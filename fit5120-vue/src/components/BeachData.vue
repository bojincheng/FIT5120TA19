<template>
    <div class="p-4 max-w-screen-lg mx-auto">
      <h1 class="text-xl font-bold mb-4">🌊 Beach Info Dashboard</h1>
  
      <div class="mb-6">
        <button @click="activeTab = 'search'" :class="tabButtonClass('search')">Search</button>
        <button @click="activeTab = 'compare'" :class="tabButtonClass('compare')">Compare</button>
      </div>
  
      <div v-if="activeTab === 'search'">
        <div class="relative w-full mb-4 z-50">
          <input
            v-model="address"
            @input="debouncedSearch"
            @keydown.down.prevent="navigate(1)"
            @keydown.up.prevent="navigate(-1)"
            @keydown.enter.prevent="selectActiveSuggestion"
            placeholder="Search for a beach (e.g. Bondi Beach)"
            class="border p-2 rounded w-full"
          />
          <ul
            v-if="suggestions.length"
            class="absolute bg-white border shadow w-full max-h-60 overflow-auto rounded mt-1 z-50"
          >
            <li
              v-for="(item, index) in suggestions"
              :key="index"
              @click="selectSuggestion(item)"
              :class="['p-2 cursor-pointer', index === activeIndex ? 'bg-blue-100' : 'hover:bg-gray-100']"
            >
              {{ item.display_name }}
            </li>
          </ul>
        </div>
  
        <div v-if="loading" class="text-blue-600 mb-2">Loading weather & marine data...</div>
        <div v-if="error" class="text-red-500 mb-2">{{ error }}</div>
  
        <div v-if="weather?.current && marine" class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h2 class="font-bold">Weather Data</h2>
            <p>Temperature: {{ weather.current.temperature_2m?.toFixed(2) }} °C</p>
            <p>Wind Speed: {{ weather.current.wind_speed_10m?.toFixed(2) }} km/h</p>
            <p>Weather: {{ weatherName }}</p>
            <p>Today's UV Index Max: {{ todayUV?.toFixed(2) }}</p>
          </div>
          <div>
            <h2 class="font-bold">Marine Data</h2>
            <p>Wave Height: {{ marine.wave_height?.toFixed(2) }} m</p>
            <p>Swell Height: {{ marine.swell_wave_height?.toFixed(2) }} m</p>
            <p>Ocean Current Velocity: {{ marine.ocean_current_velocity?.toFixed(2) }} m/s</p>
            <p>Sea Surface Temp: {{ marine.sea_surface_temperature?.toFixed(2) }} °C</p>
            <p>Sea Level Height: {{ marine.sea_level_height_msl?.toFixed(2) }} m</p>
          </div>
        </div>
      </div>
  
      <div v-else-if="activeTab === 'compare'">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
          <div class="relative">
            <input
              v-model="compareAddress1"
              @input="debouncedSearchCompare1"
              placeholder="Enter first beach (e.g. Bondi Beach)"
              class="border p-2 rounded w-full"
            />
            <ul
              v-if="suggestions1.length"
              class="absolute bg-white border shadow w-full max-h-60 overflow-auto rounded mt-1 z-50"
            >
              <li
                v-for="(item, index) in suggestions1"
                :key="index"
                @click="selectCompareSuggestion(item, 1)"
                class="p-2 cursor-pointer hover:bg-gray-100"
              >
                {{ item.display_name }}
              </li>
            </ul>
          </div>
  
          <div class="relative">
            <input
              v-model="compareAddress2"
              @input="debouncedSearchCompare2"
              placeholder="Enter second beach (e.g. Qingdao Beach)"
              class="border p-2 rounded w-full"
            />
            <ul
              v-if="suggestions2.length"
              class="absolute bg-white border shadow w-full max-h-60 overflow-auto rounded mt-1 z-50"
            >
              <li
                v-for="(item, index) in suggestions2"
                :key="index"
                @click="selectCompareSuggestion(item, 2)"
                class="p-2 cursor-pointer hover:bg-gray-100"
              >
                {{ item.display_name }}
              </li>
            </ul>
          </div>
        </div>
  
        <button
          @click="fetchCompareBeaches"
          :disabled="!selectedBeach1 || !selectedBeach2"
          class="px-4 py-2 bg-blue-500 text-white rounded mb-4 disabled:opacity-50"
        >
          Compare
        </button>
  
        <BarChart v-if="compareChartData" :chart-data="compareChartData" />
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import { debounce } from 'lodash';
  import BarChart from './BarChart.vue';
  
  export default {
    components: { BarChart },
    setup() {
      const activeTab = ref('search');
      const address = ref('');
      const suggestions = ref([]);
      const suggestions1 = ref([]);
      const suggestions2 = ref([]);
      const activeIndex = ref(-1);
      const loading = ref(false);
      const error = ref(null);
      const weather = ref(null);
      const marine = ref(null);
  
      const compareAddress1 = ref('');
      const compareAddress2 = ref('');
      const selectedBeach1 = ref(null);
      const selectedBeach2 = ref(null);
      const compareWeather1 = ref(null);
      const compareMarine1 = ref(null);
      const compareWeather2 = ref(null);
      const compareMarine2 = ref(null);
  
      const weatherCodeMap = {
        0: 'Clear sky', 1: 'Mainly clear', 2: 'Partly cloudy', 3: 'Overcast',
        45: 'Fog', 51: 'Light drizzle', 61: 'Light rain', 71: 'Light snow',
        80: 'Rain showers', 95: 'Thunderstorm'
      };
  
      const weatherName = computed(() => {
        const code = weather.value?.current?.weather_code;
        return weatherCodeMap[code] || 'Unknown';
      });
  
      const todayUV = computed(() => weather.value?.daily_uv_index_max?.[0]?.uv_index_max ?? 'N/A');
  
      const fetchSuggestions = async (query, target, country = null) => {
        if (query.length < 2) {
          target.value = [];
          return;
        }
        try {
          const base = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=5`;
          const url = country ? `${base}&countrycodes=${country}` : base;
          const res = await fetch(url, { headers: { 'User-Agent': 'BeachApp/1.0' } });
          target.value = await res.json();
        } catch (err) {
          target.value = [];
        }
      };
  
      const debouncedSearch = debounce(() => fetchSuggestions(address.value, suggestions, 'au'), 300);
      const debouncedSearchCompare1 = debounce(() => fetchSuggestions(compareAddress1.value, suggestions1), 300);
      const debouncedSearchCompare2 = debounce(() => fetchSuggestions(compareAddress2.value, suggestions2), 300);
  
      const selectCompareSuggestion = (item, which) => {
        if (which === 1) {
          compareAddress1.value = item.display_name;
          suggestions1.value = [];
          selectedBeach1.value = item;
        } else {
          compareAddress2.value = item.display_name;
          suggestions2.value = [];
          selectedBeach2.value = item;
        }
      };
  
      const fetchBeachData = async (lat, lon) => {
        const [weatherRes, marineRes] = await Promise.all([
          fetch(`https://fit5120ta19.onrender.com/weather?latitude=${lat}&longitude=${lon}`),
          fetch(`https://fit5120ta19.onrender.com/marine?latitude=${lat}&longitude=${lon}`)
        ]);
        return {
          weather: await weatherRes.json(),
          marine: await marineRes.json()
        };
      };
  
      const selectSuggestion = async (item) => {
        address.value = item.display_name;
        suggestions.value = [];
        activeIndex.value = -1;
        const lat = parseFloat(item.lat);
        const lon = parseFloat(item.lon);
        loading.value = true;
        const { weather: w, marine: m } = await fetchBeachData(lat, lon);
        weather.value = w;
        marine.value = m;
        loading.value = false;
      };
  
      const fetchCompareBeaches = async () => {
        const [lat1, lon1] = [parseFloat(selectedBeach1.value.lat), parseFloat(selectedBeach1.value.lon)];
        const [lat2, lon2] = [parseFloat(selectedBeach2.value.lat), parseFloat(selectedBeach2.value.lon)];
        const [data1, data2] = await Promise.all([
          fetchBeachData(lat1, lon1),
          fetchBeachData(lat2, lon2)
        ]);
        compareWeather1.value = data1.weather;
        compareMarine1.value = data1.marine;
        compareWeather2.value = data2.weather;
        compareMarine2.value = data2.marine;
      };
  
      const compareChartData = computed(() => {
        if (!compareWeather1.value?.current || !compareWeather2.value?.current || !compareMarine1.value || !compareMarine2.value) return null;

        return {
            labels: [
            'Temperature (°C)',
            'Wind Speed (km/h)',
            'UV Index',
            'Wave Height (m)',
            'Swell Height (m)',
            'Ocean Current Velocity (m/s)',
            'Sea Surface Temp (°C)',
            'Sea Level Height (m)'
            ],
            datasets: [
            {
                label: selectedBeach1.value.display_name,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                data: [
                compareWeather1.value.current.temperature_2m,
                compareWeather1.value.current.wind_speed_10m,
                compareWeather1.value.daily_uv_index_max?.[0]?.uv_index_max,
                compareMarine1.value.wave_height,
                compareMarine1.value.swell_wave_height,
                compareMarine1.value.ocean_current_velocity,
                compareMarine1.value.sea_surface_temperature,
                compareMarine1.value.sea_level_height_msl
                ]
            },
            {
                label: selectedBeach2.value.display_name,
                backgroundColor: 'rgba(255, 99, 132, 0.6)',
                data: [
                compareWeather2.value.current.temperature_2m,
                compareWeather2.value.current.wind_speed_10m,
                compareWeather2.value.daily_uv_index_max?.[0]?.uv_index_max,
                compareMarine2.value.wave_height,
                compareMarine2.value.swell_wave_height,
                compareMarine2.value.ocean_current_velocity,
                compareMarine2.value.sea_surface_temperature,
                compareMarine2.value.sea_level_height_msl
                ]
            }
          ]
        };
      });
  
      const chartOptions = {
        responsive: true,
        plugins: {
          legend: { position: 'top' },
          title: { display: true, text: 'Weather Comparison Between Two Beaches' }
        }
      };
  
      const navigate = (step) => {
        if (!suggestions.value.length) return;
        activeIndex.value = (activeIndex.value + step + suggestions.value.length) % suggestions.value.length;
      };
  
      const selectActiveSuggestion = () => {
        if (activeIndex.value >= 0 && activeIndex.value < suggestions.value.length) {
          selectSuggestion(suggestions.value[activeIndex.value]);
        }
      };
  
      const tabButtonClass = (tab) => [
        'px-4 py-2 border rounded-t-md font-semibold',
        activeTab.value === tab ? 'bg-white border-b-transparent' : 'bg-gray-100 border-b-gray-300'
      ];
  
      return {
        address,
        suggestions,
        suggestions1,
        suggestions2,
        activeIndex,
        compareAddress1,
        compareAddress2,
        selectedBeach1,
        selectedBeach2,
        compareWeather1,
        compareWeather2,
        compareMarine1,
        compareMarine2,
        activeTab,
        debouncedSearch,
        debouncedSearchCompare1,
        debouncedSearchCompare2,
        navigate,
        selectCompareSuggestion,
        selectActiveSuggestion,
        selectSuggestion,
        fetchCompareBeaches,
        loading,
        error,
        weather,
        marine,
        weatherName,
        todayUV,
        tabButtonClass,
        //chartCompareData,
        chartOptions,
        compareChartData
      };
    }
  };
  </script>