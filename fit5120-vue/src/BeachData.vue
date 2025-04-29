<template>
    <div style="padding: 1rem; max-width: 1024px; margin: 0 auto;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
        <button @click="goBack" style="display: flex; align-items: center; color: #3B82F6; cursor: pointer;">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          <span style="margin-left: 0.25rem;">Back to Beach Safety</span>
        </button>
        <h1 style="font-size: 1.25rem; font-weight: bold;">🌊 Beach Info Dashboard</h1>
      </div>
  
      <div style="margin-bottom: 1.5rem;">
        <button @click="activeTab = 'search'" :style="activeTab === 'search' ? 'padding: 0.5rem 1rem; border: 1px solid #D1D5DB; border-radius: 0.375rem 0.375rem 0 0; font-weight: 600; background-color: white; border-bottom-color: transparent;' : 'padding: 0.5rem 1rem; border: 1px solid #D1D5DB; border-radius: 0.375rem 0.375rem 0 0; font-weight: 600; background-color: #F3F4F6;'">Search</button>
        <button @click="activeTab = 'compare'" :style="activeTab === 'compare' ? 'padding: 0.5rem 1rem; border: 1px solid #D1D5DB; border-radius: 0.375rem 0.375rem 0 0; font-weight: 600; background-color: white; border-bottom-color: transparent;' : 'padding: 0.5rem 1rem; border: 1px solid #D1D5DB; border-radius: 0.375rem 0.375rem 0 0; font-weight: 600; background-color: #F3F4F6;'">Compare</button>
      </div>
  
      <div v-if="activeTab === 'search'">
        <div style="position: relative; width: 90%; margin-bottom: 1rem; z-index: 50; margin-left: auto; margin-right: auto;">
          <input
            v-model="address"
            @input="debouncedSearch"
            @keydown.down.prevent="navigate(1)"
            @keydown.up.prevent="navigate(-1)"
            @keydown.enter.prevent="selectActiveSuggestion"
            placeholder="Search for a beach (e.g. Bondi Beach)"
            style="border: 1px solid #D1D5DB; padding: 0.5rem; border-radius: 0.25rem; width: 100%;"
          />
          <ul
            v-if="suggestions.length"
            style="position: absolute; background-color: white; border: 1px solid #D1D5DB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); width: 100%; max-height: 15rem; overflow: auto; border-radius: 0.25rem; margin-top: 0.25rem; z-index: 50;"
          >
            <li
              v-for="(item, index) in suggestions"
              :key="index"
              @click="selectSuggestion(item)"
              :style="[
                'padding: 0.5rem; cursor: pointer;', 
                index === activeIndex ? 'background-color: #EFF6FF;' : 'hover:background-color: #F3F4F6;'
              ]"
            >
              {{ item.display_name }}
            </li>
          </ul>
        </div>
  
        <div v-if="loading" style="color: #2563EB; margin-bottom: 0.5rem; text-align: center;">Loading weather & marine data...</div>
        <div v-if="error" style="color: #EF4444; margin-bottom: 0.5rem; text-align: center;">{{ error }}</div>
  
        <div v-if="weather?.current && marine" style="display: grid; grid-template-columns: 1fr; gap: 1rem; width: 90%; margin-left: auto; margin-right: auto;">
          <div>
            <h2 style="font-weight: bold;">Weather Data</h2>
            <p>Temperature: {{ weather.current.temperature_2m?.toFixed(2) }} °C</p>
            <p>Wind Speed: {{ weather.current.wind_speed_10m?.toFixed(2) }} km/h</p>
            <p>Weather: {{ weatherName }}</p>
            <p>Today's UV Index Max: {{ todayUV?.toFixed(2) }}</p>
          </div>
          <div>
            <h2 style="font-weight: bold;">Marine Data</h2>
            <p>Wave Height: {{ marine.wave_height?.toFixed(2) }} m</p>
            <p>Swell Height: {{ marine.swell_wave_height?.toFixed(2) }} m</p>
            <p>Ocean Current Velocity: {{ marine.ocean_current_velocity?.toFixed(2) }} m/s</p>
            <p>Sea Surface Temp: {{ marine.sea_surface_temperature?.toFixed(2) }} °C</p>
            <p>Sea Level Height: {{ marine.sea_level_height_msl?.toFixed(2) }} m</p>
          </div>
        </div>
      </div>
  
      <div v-else-if="activeTab === 'compare'">
        <div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin-bottom: 1rem; width: 90%; margin-left: auto; margin-right: auto;">
          <div style="position: relative;">
            <input
              v-model="compareAddress1"
              @input="debouncedSearchCompare1"
              placeholder="Enter first beach (e.g. Bondi Beach)"
              style="border: 1px solid #D1D5DB; padding: 0.5rem; border-radius: 0.25rem; width: 100%;"
            />
            <ul
              v-if="suggestions1.length"
              style="position: absolute; background-color: white; border: 1px solid #D1D5DB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); width: 100%; max-height: 15rem; overflow: auto; border-radius: 0.25rem; margin-top: 0.25rem; z-index: 50;"
            >
              <li
                v-for="(item, index) in suggestions1"
                :key="index"
                @click="selectCompareSuggestion(item, 1)"
                style="padding: 0.5rem; cursor: pointer; background-color: #F3F4F6;"
              >
                {{ item.display_name }}
              </li>
            </ul>
          </div>
  
          <div style="position: relative;">
            <input
              v-model="compareAddress2"
              @input="debouncedSearchCompare2"
              placeholder="Enter second beach (e.g. Qingdao Beach)"
              style="border: 1px solid #D1D5DB; padding: 0.5rem; border-radius: 0.25rem; width: 100%;"
            />
            <ul
              v-if="suggestions2.length"
              style="position: absolute; background-color: white; border: 1px solid #D1D5DB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); width: 100%; max-height: 15rem; overflow: auto; border-radius: 0.25rem; margin-top: 0.25rem; z-index: 50;"
            >
              <li
                v-for="(item, index) in suggestions2"
                :key="index"
                @click="selectCompareSuggestion(item, 2)"
                style="padding: 0.5rem; cursor: pointer; background-color: #F3F4F6;"
              >
                {{ item.display_name }}
              </li>
            </ul>
          </div>
        </div>
  
        <button
          @click="fetchCompareBeaches"
          :disabled="!selectedBeach1 || !selectedBeach2 || loading"
          :style="{
            padding: '0.5rem 1rem',
            backgroundColor: '#3B82F6',
            color: 'white',
            borderRadius: '0.25rem',
            marginBottom: '1rem',
            cursor: 'pointer',
            opacity: (loading || !selectedBeach1 || !selectedBeach2) ? 0.5 : 1,
            width: '50%',
            marginLeft: 'auto',
            marginRight: 'auto',
            display: 'block'
          }"
        >
          {{ loading ? 'Loading...' : 'Compare' }}
        </button>
  
        <div v-if="error" style="color: #EF4444; margin-bottom: 1rem; text-align: center; width: 90%; margin-left: auto; margin-right: auto;">{{ error }}</div>
  
        <div v-if="loading" style="width: 90%; margin: 2rem auto; text-align: center; padding: 2rem; background-color: #f3f4f6; border-radius: 0.5rem;">
          <div style="color: #3B82F6; font-weight: 600; margin-bottom: 0.5rem;">Loading comparison data...</div>
          <div style="color: #6B7280; font-size: 0.9rem;">This might take a few seconds.</div>
        </div>
  
        <div v-else-if="compareChartData" style="width: 90%; margin: 0 auto;">
          <h3 style="text-align: center; margin-bottom: 1rem;">Comparing: {{ selectedBeach1?.display_name?.split(',')[0] }} vs {{ selectedBeach2?.display_name?.split(',')[0] }}</h3>
          <BarChart 
            :chart-data="compareChartData" 
            :chart-title="`Comparing ${selectedBeach1?.display_name?.split(',')[0]} vs ${selectedBeach2?.display_name?.split(',')[0]}`"
            style="display: block; height: 450px;" 
          />
        </div>
        
        <div v-else-if="!loading && selectedBeach1 && selectedBeach2" style="text-align: center; padding: 2rem; color: #6B7280;">
          Click the Compare button to see beach data comparison
        </div>
  
        <!-- Debug panel for development -->
        <div v-if="showDebug" style="margin-top: 2rem; border: 1px dashed #CBD5E1; padding: 1rem; font-family: monospace; background-color: #F8FAFC; border-radius: 0.5rem; width: 90%; margin-left: auto; margin-right: auto;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h3 style="font-weight: bold; margin: 0;">Debug Information</h3>
            <div>
              <button @click="fetchCompareBeaches" style="background: #10B981; color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; cursor: pointer; margin-right: 0.5rem;">Retry Compare</button>
              <button @click="showDebug = false" style="background: #EF4444; color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; cursor: pointer;">Close</button>
            </div>
          </div>
          <div>
            <p><strong>Beach 1:</strong> {{ selectedBeach1?.display_name || 'Not selected' }}</p>
            <p style="margin-left: 1rem;"><strong>Coordinates:</strong> ({{ selectedBeach1?.lat || 'N/A' }}, {{ selectedBeach1?.lon || 'N/A' }})</p>
            <p><strong>Beach 2:</strong> {{ selectedBeach2?.display_name || 'Not selected' }}</p>
            <p style="margin-left: 1rem;"><strong>Coordinates:</strong> ({{ selectedBeach2?.lat || 'N/A' }}, {{ selectedBeach2?.lon || 'N/A' }})</p>
            
            <h4 style="margin-top: 1rem; margin-bottom: 0.5rem;">Data Status</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
              <div>
                <p><strong>Weather Data 1:</strong> {{ compareWeather1 ? '✅ Loaded' : '❌ Not loaded' }}</p>
                <p v-if="compareWeather1"><strong>Temperature:</strong> {{ compareWeather1.current?.temperature_2m ?? 'Missing' }}</p>
                <p v-if="compareWeather1"><strong>UV Index:</strong> {{ compareWeather1.daily_uv_index_max?.[0]?.uv_index_max ?? 'Missing' }}</p>
                
                <p><strong>Marine Data 1:</strong> {{ compareMarine1 ? '✅ Loaded' : '❌ Not loaded' }}</p>
                <p v-if="compareMarine1"><strong>Wave Height:</strong> {{ compareMarine1.wave_height ?? 'Missing' }}</p>
                <p v-if="compareMarine1"><strong>Ocean Current:</strong> {{ compareMarine1.ocean_current_velocity ?? 'Missing' }}</p>
              </div>
              <div>
                <p><strong>Weather Data 2:</strong> {{ compareWeather2 ? '✅ Loaded' : '❌ Not loaded' }}</p>
                <p v-if="compareWeather2"><strong>Temperature:</strong> {{ compareWeather2.current?.temperature_2m ?? 'Missing' }}</p>
                <p v-if="compareWeather2"><strong>UV Index:</strong> {{ compareWeather2.daily_uv_index_max?.[0]?.uv_index_max ?? 'Missing' }}</p>
                
                <p><strong>Marine Data 2:</strong> {{ compareMarine2 ? '✅ Loaded' : '❌ Not loaded' }}</p>
                <p v-if="compareMarine2"><strong>Wave Height:</strong> {{ compareMarine2.wave_height ?? 'Missing' }}</p>
                <p v-if="compareMarine2"><strong>Ocean Current:</strong> {{ compareMarine2.ocean_current_velocity ?? 'Missing' }}</p>
              </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
              <button @click="error = null" style="background: #3B82F6; color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; cursor: pointer;">Clear Errors</button>
              <button @click="() => { compareWeather1 = null; compareMarine1 = null; compareWeather2 = null; compareMarine2 = null; }" style="background: #6B7280; color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; cursor: pointer;">Reset Data</button>
            </div>
          </div>
        </div>
  
        <!-- Add debug toggle button in a non-intrusive spot -->
        <div style="position: fixed; bottom: 1rem; right: 1rem; z-index: 100;">
          <button @click="showDebug = !showDebug" style="background: rgba(0,0,0,0.5); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; cursor: pointer; font-size: 0.75rem;">{{ showDebug ? 'Hide Debug' : 'Debug' }}</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import BarChart from './BarChart.vue';
  
  // Simple debounce implementation
  function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }
  
  export default {
    components: { BarChart },
    setup() {
      const router = useRouter();
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
      const showDebug = ref(true);
  
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
          if (!res.ok) {
            throw new Error(`Search failed with status: ${res.status}`);
          }
          target.value = await res.json();
        } catch (err) {
          console.error('Search error:', err);
          error.value = `Failed to search: ${err.message}`;
          target.value = [];
        }
      };
  
      const debouncedSearch = debounce(() => fetchSuggestions(address.value, suggestions, 'au'), 300);
      const debouncedSearchCompare1 = debounce(() => fetchSuggestions(compareAddress1.value, suggestions1), 300);
      const debouncedSearchCompare2 = debounce(() => fetchSuggestions(compareAddress2.value, suggestions2), 300);
  
      const selectCompareSuggestion = (item, which) => {
        try {
          console.log(`Selected beach ${which}:`, item);
          
          if (which === 1) {
            compareAddress1.value = item.display_name;
            suggestions1.value = [];
            selectedBeach1.value = item;
          } else {
            compareAddress2.value = item.display_name;
            suggestions2.value = [];
            selectedBeach2.value = item;
          }
          
          // Reset any existing error messages
          error.value = null;
          
          console.log('Beach selection state:', {
            beach1: selectedBeach1.value?.display_name,
            beach2: selectedBeach2.value?.display_name
          });
        } catch (err) {
          console.error('Error selecting beach:', err);
          error.value = `Error selecting beach: ${err.message}`;
        }
      };
  
      const fetchBeachData = async (lat, lon) => {
        console.log(`Requesting data for coordinates: (${lat}, ${lon})`);
        
        try {
          // Check for valid coordinates
          if (isNaN(lat) || isNaN(lon) || lat === 0 || lon === 0) {
            throw new Error(`Invalid coordinates: (${lat}, ${lon})`);
          }
          
          // Log API URLs for debugging
          const weatherUrl = `https://fit5120ta19.onrender.com/weather?latitude=${lat}&longitude=${lon}`;
          const marineUrl = `https://fit5120ta19.onrender.com/marine?latitude=${lat}&longitude=${lon}`;
          console.log('Weather API URL:', weatherUrl);
          console.log('Marine API URL:', marineUrl);
          
          // Add timeout to API requests
          const fetchWithTimeout = (url, options = {}, timeout = 20000) => {
            return Promise.race([
              fetch(url, options),
              new Promise((_, reject) => 
                setTimeout(() => reject(new Error(`Request timed out after ${timeout}ms`)), timeout)
              )
            ]);
          };
          
          let weatherRes, marineRes;
          
          try {
            // Use Promise.all for parallel requests with timeouts
            [weatherRes, marineRes] = await Promise.all([
              fetchWithTimeout(weatherUrl),
              fetchWithTimeout(marineUrl)
            ]);
          } catch (err) {
            console.error('API request timeout or network error:', err);
            throw new Error(`Network issue: ${err.message}. Please check your connection and try again.`);
          }
          
          if (!weatherRes.ok) {
            throw new Error(`Weather API failed with status: ${weatherRes.status}`);
          }
          
          if (!marineRes.ok) {
            throw new Error(`Marine API failed with status: ${marineRes.status}`);
          }
          
          let weather, marine;
          
          try {
            weather = await weatherRes.json();
          } catch (err) {
            console.error('Failed to parse weather response:', err);
            throw new Error('Weather data format error. Please try again later.');
          }
          
          try {
            marine = await marineRes.json();
          } catch (err) {
            console.error('Failed to parse marine response:', err);
            throw new Error('Marine data format error. Please try again later.');
          }
          
          // Validate response data
          if (!weather?.current) {
            console.error('Invalid weather data structure:', weather);
            throw new Error('Weather API returned incomplete data');
          }
          
          if (marine.wave_height === undefined) {
            console.error('Invalid marine data structure:', marine);
            throw new Error('Marine API returned incomplete data');
          }
          
          console.log('API request successful');
          console.log('Weather data sample:', { 
            temp: weather.current.temperature_2m, 
            wind: weather.current.wind_speed_10m 
          });
          console.log('Marine data sample:', { 
            wave: marine.wave_height, 
            current: marine.ocean_current_velocity 
          });
          
          return { weather, marine };
        } catch (err) {
          console.error('API fetch error:', err);
          error.value = `Failed to fetch data: ${err.message}`;
          return { weather: null, marine: null };
        }
      };
  
      const selectSuggestion = async (item) => {
        address.value = item.display_name;
        suggestions.value = [];
        activeIndex.value = -1;
        const lat = parseFloat(item.lat);
        const lon = parseFloat(item.lon);
        loading.value = true;
        error.value = null;
        
        try {
          const { weather: w, marine: m } = await fetchBeachData(lat, lon);
          if (w && m) {
            weather.value = w;
            marine.value = m;
          } else {
            error.value = 'Could not retrieve beach data. Please try another location.';
          }
        } catch (err) {
          error.value = `Error: ${err.message}`;
        } finally {
          loading.value = false;
        }
      };
  
      const fetchCompareBeaches = async () => {
        if (!selectedBeach1.value || !selectedBeach2.value) {
          console.warn('Cannot compare beaches: One or both beaches not selected');
          error.value = 'Please select two beaches to compare.';
          return;
        }
        
        loading.value = true;
        error.value = null;
        
        // Reset any previous comparison data to avoid stale data display
        compareWeather1.value = null;
        compareMarine1.value = null; 
        compareWeather2.value = null;
        compareMarine2.value = null;
        
        try {
          const [lat1, lon1] = [parseFloat(selectedBeach1.value.lat), parseFloat(selectedBeach1.value.lon)];
          const [lat2, lon2] = [parseFloat(selectedBeach2.value.lat), parseFloat(selectedBeach2.value.lon)];
          
          console.log(`Fetching data for beaches: 
            1) ${selectedBeach1.value.display_name} (${lat1}, ${lon1})
            2) ${selectedBeach2.value.display_name} (${lat2}, ${lon2})`);
          
          // Sequential fetches for better error identification
          const data1 = await fetchBeachData(lat1, lon1);
          if (!data1.weather || !data1.marine) {
            throw new Error(`Could not retrieve data for ${selectedBeach1.value.display_name}`);
          }
          
          const data2 = await fetchBeachData(lat2, lon2);
          if (!data2.weather || !data2.marine) {
            throw new Error(`Could not retrieve data for ${selectedBeach2.value.display_name}`);
          }
          
          // Data validation passed, set the comparison data
          compareWeather1.value = data1.weather;
          compareMarine1.value = data1.marine;
          compareWeather2.value = data2.weather;
          compareMarine2.value = data2.marine;
          
          // Force update the computed value
          console.log('Beach 1 marine data properties:', Object.keys(compareMarine1.value));
          console.log('Beach 2 marine data properties:', Object.keys(compareMarine2.value));
          console.log('Comparison data loaded successfully');
          
          // Show debug automatically if available
          showDebug.value = true;
        } catch (err) {
          console.error('Compare beaches error:', err);
          error.value = `Failed to compare beaches: ${err.message}`;
        } finally {
          loading.value = false;
        }
      };
  
      const compareChartData = computed(() => {
        if (!compareWeather1.value?.current || !compareWeather2.value?.current || 
            !compareMarine1.value || !compareMarine2.value) {
          console.log('Missing comparison data, cannot create chart');
          return null;
        }
  
        const beach1Name = selectedBeach1.value.display_name.split(',')[0];
        const beach2Name = selectedBeach2.value.display_name.split(',')[0];
        
        console.log(`Creating chart for ${beach1Name} vs ${beach2Name}`);
  
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
              label: beach1Name,
              backgroundColor: 'rgba(54, 162, 235, 0.6)',
              data: [
                compareWeather1.value.current.temperature_2m || 0,
                compareWeather1.value.current.wind_speed_10m || 0,
                compareWeather1.value.daily_uv_index_max?.[0]?.uv_index_max || 0,
                compareMarine1.value.wave_height || 0,
                compareMarine1.value.swell_wave_height || 0,
                compareMarine1.value.ocean_current_velocity || 0,
                compareMarine1.value.sea_surface_temperature || 0,
                compareMarine1.value.sea_level_height_msl || 0
              ]
            },
            {
              label: beach2Name,
              backgroundColor: 'rgba(255, 99, 132, 0.6)',
              data: [
                compareWeather2.value.current.temperature_2m || 0,
                compareWeather2.value.current.wind_speed_10m || 0,
                compareWeather2.value.daily_uv_index_max?.[0]?.uv_index_max || 0,
                compareMarine2.value.wave_height || 0,
                compareMarine2.value.swell_wave_height || 0,
                compareMarine2.value.ocean_current_velocity || 0,
                compareMarine2.value.sea_surface_temperature || 0,
                compareMarine2.value.sea_level_height_msl || 0
              ]
            }
          ]
        };
      });
  
      const navigate = (step) => {
        if (!suggestions.value.length) return;
        activeIndex.value = (activeIndex.value + step + suggestions.value.length) % suggestions.value.length;
      };
  
      const selectActiveSuggestion = () => {
        if (activeIndex.value >= 0 && activeIndex.value < suggestions.value.length) {
          selectSuggestion(suggestions.value[activeIndex.value]);
        }
      };
  
      const goBack = () => {
        router.push('/beach-safety');
      };
  
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
        compareChartData,
        goBack,
        showDebug
      };
    }
  };
  </script>
  
  <style>
  /* BarChart component now handles its own styles */
  </style>