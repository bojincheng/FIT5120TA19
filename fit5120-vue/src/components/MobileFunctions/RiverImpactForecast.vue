<template>
  <div class="river-impact-container">
    <h2>River Impact Forecast</h2>

    <div v-if="loading">Fetching your location and forecast...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else>
      <p><strong>Location:</strong> {{ latitude }}, {{ longitude }}</p>

      <table v-if="forecast.length > 0">
        <thead>
          <tr>
            <th>Date</th>
            <th>Precipitation (mm)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entry in forecast" :key="entry.date">
            <td>{{ entry.date }}</td>
            <td>{{ entry.precipitation.toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>

      <div v-else>No forecast data available.</div>

      <!-- Debug: Show raw JSON to verify data -->
      <pre style="margin-top:1rem;">{{ JSON.stringify(forecast, null, 2) }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const latitude = ref(null)
const longitude = ref(null)
const forecast = ref([])
const loading = ref(true)
const error = ref(null)

// Adapt this function if your API returns nested data
const fetchForecast = async (lat, lon) => {
  try {
    const response = await axios.get('http://localhost:5000/precipitation', {
      params: { latitude: lat, longitude: lon }
    })
    console.log('Forecast response:', response.data)

    // Example: if your API returns { hourly_forecast: { date: [...], precipitation: [...] } }
    if (response.data.hourly_forecast && response.data.hourly_forecast.date && response.data.hourly_forecast.precipitation) {
      // Map the parallel arrays into one array of objects
      forecast.value = response.data.hourly_forecast.date.map((date, index) => ({
        date,
        precipitation: response.data.hourly_forecast.precipitation[index] || 0
      }))
    } else if (Array.isArray(response.data)) {
      // If API returns a simple array
      forecast.value = response.data
    } else {
      error.value = 'Unexpected data format from API.'
    }
  } catch (err) {
    console.error(err)
    error.value = 'Failed to fetch forecast data.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        latitude.value = position.coords.latitude
        longitude.value = position.coords.longitude
        fetchForecast(latitude.value, longitude.value)
      },
      (err) => {
        error.value = 'Permission denied or location unavailable.'
        loading.value = false
      }
    )
  } else {
    error.value = 'Geolocation is not supported by your browser.'
    loading.value = false
  }
})
</script>

<style scoped>
.river-impact-container {
  padding: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f0f8ff;
}
</style>

