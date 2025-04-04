<template>
    <div class="p-4 max-w-screen-lg mx-auto">
      <h1 class="text-xl font-bold mb-4">🌊 Beach Info Dashboard</h1>
  
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
            :class="[
              'p-2 cursor-pointer',
              index === activeIndex ? 'bg-blue-100' : 'hover:bg-gray-100'
            ]"
          >
            {{ item.display_name }}
          </li>
        </ul>
      </div>
  
      <div v-if="loading" class="text-blue-600 mb-2">Loading weather & marine data...</div>
      <div v-if="error" class="text-red-500 mb-2">{{ error }}</div>
  
      <div v-if="weather && marine" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <h2 class="font-bold">Weather Data</h2>
          <p>Temperature: {{ weather.current.temperature_2m.toFixed(2) }} °C</p>
          <p>Wind Speed: {{ weather.current.wind_speed_10m.toFixed(2) }} km/h</p>
          <p>Weather: {{ weatherName }}</p>
          <p>Today's UV Index Max: {{ todayUV.toFixed(2) }}</p>
        </div>
        <div>
          <h2 class="font-bold">Marine Data</h2>
          <p>Wave Height: {{ marine.wave_height.toFixed(2)  }} m</p>
          <p>Swell Height: {{ marine.swell_wave_height.toFixed(2) }} m</p>
          <p>Ocean Current Velocity: {{ marine.ocean_current_velocity.toFixed(2) }} m/s</p>
          <p>Sea Surface Temp: {{ marine.sea_surface_temperature.toFixed(2) }} °C</p>
          <p>Sea Level Height: {{ marine.sea_level_height_msl.toFixed(2) }} m</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import { debounce } from 'lodash';
  
  export default {
    setup() {
      const address = ref('');
      const suggestions = ref([]);
      const activeIndex = ref(-1);
      const loading = ref(false);
      const error = ref(null);
      const weather = ref(null);
      const marine = ref(null);
  
      const weatherCodeMap = {
        0: 'Clear sky',
        1: 'Mainly clear',
        2: 'Partly cloudy',
        3: 'Overcast',
        45: 'Fog',
        51: 'Light drizzle',
        61: 'Light rain',
        71: 'Light snow',
        80: 'Rain showers',
        95: 'Thunderstorm'
      };
  
      const weatherName = computed(() => {
        const code = weather.value?.current?.weather_code;
        return weatherCodeMap[code] || 'Unknown';
      });
  
      const todayUV = computed(() => {
        return weather.value?.daily_uv_index_max?.[0]?.uv_index_max ?? 'N/A';
      });
  
      const debouncedSearch = debounce(async () => {
        if (address.value.length < 2) {
          suggestions.value = [];
          return;
        }
        try {
          const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address.value)}&limit=5&countrycodes=au`, {
            headers: { 'User-Agent': 'BeachApp/1.0' }
          });
          suggestions.value = await res.json();
          activeIndex.value = -1;
        } catch {
          suggestions.value = [];
        }
      }, 300);
  
      const navigate = (step) => {
        if (!suggestions.value.length) return;
        activeIndex.value = (activeIndex.value + step + suggestions.value.length) % suggestions.value.length;
      };
  
      const selectActiveSuggestion = () => {
        if (activeIndex.value >= 0 && activeIndex.value < suggestions.value.length) {
          selectSuggestion(suggestions.value[activeIndex.value]);
        }
      };
  
      const selectSuggestion = async (item) => {
        address.value = item.display_name;
        suggestions.value = [];
        activeIndex.value = -1;
        const lat = parseFloat(item.lat);
        const lon = parseFloat(item.lon);
  
        try {
          loading.value = true;
          error.value = null;
          const [weatherRes, marineRes] = await Promise.all([
            fetch(`http://localhost:5000/weather?latitude=${lat}&longitude=${lon}`),
            fetch(`http://localhost:5000/marine?latitude=${lat}&longitude=${lon}`)
          ]);
          const weatherData = await weatherRes.json();
          const marineData = await marineRes.json();
          if (!weatherRes.ok) throw new Error(weatherData.error || 'Weather fetch failed.');
          if (!marineRes.ok) throw new Error(marineData.error || 'Marine fetch failed.');
          weather.value = weatherData;
          marine.value = marineData;
        } catch (err) {
          error.value = err.message;
        } finally {
          loading.value = false;
        }
      };
  
      return {
        address,
        suggestions,
        activeIndex,
        debouncedSearch,
        navigate,
        selectActiveSuggestion,
        selectSuggestion,
        loading,
        error,
        weather,
        marine,
        weatherName,
        todayUV
      };
    }
  };
  </script>