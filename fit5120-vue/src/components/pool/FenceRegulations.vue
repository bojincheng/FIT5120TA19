<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-semibold">Pool Fence Regulations in Australia</h2>
    
    <!-- Location Input -->
    <label class="block mb-2">Enter your location (city or postcode):</label>
    <div class="flex items-center">
      <input 
        v-model="userLocation" 
        type="text" 
        placeholder="Enter your location" 
        class="p-2 border rounded w-full"
        @input="fetchLocationSuggestions"
      />
      <!-- Clear Button for Location -->
      <button 
        v-if="userLocation" 
        @click="clearLocation" 
        class="ml-2 text-gray-500 hover:text-red-500"
      >
        Clear
      </button>
    </div>
    
    <!-- Error Message -->
    <div v-if="errorMessage" class="text-red-600 mt-2">
      {{ errorMessage }}
    </div>
    
    <!-- Suggestions -->
    <ul v-if="locationSuggestions.length" class="mt-2 bg-white border rounded shadow-md">
      <li 
        v-for="(suggestion, index) in locationSuggestions" 
        :key="index" 
        @click="selectLocation(suggestion)" 
        class="p-2 cursor-pointer hover:bg-gray-200"
      >
        {{ suggestion.display_name }}
      </li>
    </ul>

    <!-- Show detected location -->
    <div v-if="selectedLocation" class="mt-4 text-sm text-gray-700">
      <p>You selected: <strong>{{ selectedLocation.display_name }}</strong></p>
      <p v-if="autoDetectedState">Auto-detected state: <strong>{{ autoDetectedState }}</strong></p>
      <p v-else class="text-red-600">Could not detect state from location. Please select manually below.</p>
    </div>

    <!-- Manual state override -->
    <div class="mt-4">
      <label class="block mb-2 font-medium">Select a state to view regulations:</label>
      <div class="flex items-center">
        <select v-model="selectedState" class="p-2 border rounded w-full">
          <option value="" disabled>Select a state</option>
          <option v-for="(label, key) in stateOptions" :key="key" :value="key">
            {{ label }}
          </option>
        </select>
        <!-- Clear Button for State -->
        <button 
          v-if="selectedState" 
          @click="clearState" 
          class="ml-2 text-gray-500 hover:text-red-500"
        >
          Clear
        </button>
      </div>
    </div>

    <!-- Show regulation info -->
    <div v-if="selectedState" class="mt-4 bg-blue-50 p-4 rounded">
      <h3 class="text-lg font-bold">{{ stateOptions[selectedState] }} Regulations</h3>
      <ul class="list-disc pl-5">
        <li>Minimum Fence Height: {{ regulations[selectedState].height }}</li>
        <li>Gap Limits: {{ regulations[selectedState].gaps }}</li>
        <li>Self-closing Gate: {{ regulations[selectedState].selfClosing ? 'Yes' : 'No' }}</li>
        <li>Pool Registration Requirement: {{ regulations[selectedState].registration }}</li>
        <li>Inspection Frequency: {{ regulations[selectedState].inspection }}</li>
        <li>Additional Requirements: {{ regulations[selectedState].additional }}</li>
      </ul>
    </div>

    <!-- Disclaimer -->
    <div class="mt-8 text-center text-sm text-gray-500">
      <p>
        These regulations are based on the latest available data. For the most accurate and up-to-date information, refer to the official resource below:
      </p>
      <p>
        <a href="https://www.royallifesaving.com.au/__data/assets/pdf_file/0014/74021/Royal-Life-Saving-Review-of-Pool-Fencing-Legistration-in-Australia.pdf" target="_blank" class="text-blue-600 underline">
          Royal Life Saving Australia - Review of Pool Fencing Legislation (PDF)
        </a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const userLocation = ref('');
const locationSuggestions = ref([]);
const selectedLocation = ref(null);
const autoDetectedState = ref('');
const selectedState = ref('');
const errorMessage = ref('');

const stateOptions = {
  VIC: 'Victoria',
  NSW: 'New South Wales',
  QLD: 'Queensland',
  SA: 'South Australia',
  WA: 'Western Australia',
  NT: 'Northern Territory',
  TAS: 'Tasmania'
};

const regulations = {
  VIC: {
    height: '1.2m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 4 years',
    additional: 'Safety signage required, CPR signs must be displayed'
  },
  NSW: {
    height: '1.2m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 3 years',
    additional: 'Compliance certificate required for property sale or lease'
  },
  QLD: {
    height: '1.2m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 2 years',
    additional: 'Additional rules apply for temporary or inflatable pools'
  },
  SA: {
    height: '1.8m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 4 years',
    additional: 'All gates must be child-proof, with no access to pool area by pets'
  },
  WA: {
    height: '1.8m minimum',
    gaps: 'No more than 100mm',
    selfClosing: false,
    registration: 'Required for all pools',
    inspection: 'Every 3 years',
    additional: 'Gates must open outward and be self-latching'
  },
  NT: {
    height: '1.2m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 5 years',
    additional: 'Pools must be registered with local council and meet safety guidelines'
  },
  TAS: {
    height: '1.2m minimum',
    gaps: 'No more than 100mm',
    selfClosing: true,
    registration: 'Required for all pools',
    inspection: 'Every 3 years',
    additional: 'Temporary pools must be fenced and comply with full pool regulations'
  }
};

// Watch auto-detected state and update selection automatically
watch(autoDetectedState, (val) => {
  if (val && regulations[val]) {
    selectedState.value = val;
  }
});

// Fetch location suggestions and check if it's in Australia
const fetchLocationSuggestions = async () => {
  if (userLocation.value.length > 2) {
    const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&addressdetails=1&q=${userLocation.value}`);
    const data = await response.json();
    
    // Filter to show only Australian locations
    const australianLocations = data.filter(location => location.address.country === 'Australia');
    
    if (australianLocations.length === 0) {
      errorMessage.value = 'Location not found or not in Australia. Please enter a valid Australian location.';
      locationSuggestions.value = [];
    } else {
      errorMessage.value = '';  // Clear error message
      locationSuggestions.value = australianLocations;
    }
  } else {
    locationSuggestions.value = [];
    errorMessage.value = '';  // Clear error message
  }
};

// When user selects a location
const selectLocation = (location) => {
  userLocation.value = location.display_name;
  selectedLocation.value = location;
  locationSuggestions.value = [];

  const stateName = location.address.state || location.address.state_district || location.address.region || '';
  const reverseStateMap = {
    'Victoria': 'VIC',
    'New South Wales': 'NSW',
    'Queensland': 'QLD',
    'South Australia': 'SA',
    'Western Australia': 'WA',
    'Northern Territory': 'NT',
    'Tasmania': 'TAS'
  };

  const abbreviation = reverseStateMap[stateName];
  autoDetectedState.value = abbreviation || '';
};

// Clear the location input and suggestions
const clearLocation = () => {
  userLocation.value = '';
  locationSuggestions.value = [];
  errorMessage.value = '';
  selectedLocation.value = null;
  autoDetectedState.value = '';
  selectedState.value = '';
};

// Clear the selected state
const clearState = () => {
  selectedState.value = '';
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
  margin-top: 0.5rem;
}

li {
  padding: 0.5rem;
  cursor: pointer;
  background-color: #fff;
}

li:hover {
  background-color: #f1f1f1;
}

.text-blue-600:hover {
  text-decoration: underline;
}
</style>


