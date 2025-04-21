<template>
  <div>
    <h2>Drowning Statistics Search</h2>

    <!-- Drowning Deaths Search Section -->
    <h3>Search Drowning Deaths</h3>

    <label for="age">Select Age Group:</label>
    <select v-model="deathSearchCriteria.age_group" id="age">
      <option value="">All</option>
      <option value="0-4">0-4 years</option>
      <option value="5-14">5-14 years</option>
      <option value="15-24">15-24 years</option>
      <option value="25-44">25-44 years</option>
      <option value="45-64">45-64 years</option>
      <option value="65+">65+ years</option>
    </select>

    <label for="location">Select Location:</label>
    <select v-model="deathSearchCriteria.location" id="location">
      <option value="">All Locations</option>
      <option value="Natural water">Natural water</option>
      <option value="Swimming pool">Swimming pool</option>
      <option value="Bathtub">Bathtub</option>
      <option value="Other or unspecified">Other or unspecified</option>
      <option value="Elsewhere classified">Elsewhere classified</option>
    </select>

    <button @click="searchDeaths">Search Deaths</button>
    <button @click="clearFilters">Clear</button>

    <h3>Search Drowning Injuries</h3>
    <label for="injury-age">Select Age Group:</label>
    <select v-model="injurySearchCriteria.age_group" id="injury-age">
      <option value="">All</option>
      <option value="0-4">0-4 years</option>
      <option value="5-14">5-14 years</option>
      <option value="15-24">15-24 years</option>
      <option value="25-44">25-44 years</option>
      <option value="45-64">45-64 years</option>
      <option value="65+">65+ years</option>
    </select>

    <label for="injury-location">Select Location:</label>
    <select v-model="injurySearchCriteria.location" id="injury-location">
      <option value="">All Locations</option>
      <option value="Natural water">Natural water</option>
      <option value="Swimming pool">Swimming pool</option>
      <option value="Bathtub">Bathtub</option>
      <option value="Other or unspecified">Other or unspecified</option>
    </select>

    <button @click="searchInjuries">Search Injuries</button>
    <button @click="clearFilters">Clear</button>

    <!-- Display Results -->
    <div v-if="results.length">
      <h3>Search Results:</h3>
      <table>
        <thead>
          <tr>
            <th>Location</th>
            <th>Age Group</th>
            <th>Deaths / Cases</th>
            <th v-if="isDeathSearch">Rate (per 100,00000 population)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(result, index) in results" :key="index">
            <td>{{ result.location }}</td>
            <td>{{ result.age_group || "All age groups" }}</td>
            <td>
              <span v-if="isDeathSearch">{{ result.deaths }} deaths</span>
              <span v-else>{{ result.cases }} cases</span>
            </td>
            <td v-if="isDeathSearch">
              {{ result.rate !== null && result.rate !== undefined ? parseInt(result.rate) : "N/A" }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- No Results Message -->
    <div v-else-if="isNoResults">
      <p>No drowning data found based on your selection. Try adjusting the filters.</p>
    </div>

    <!-- Error Message -->
    <div v-if="errorMessage" class="error-message">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      deathSearchCriteria: {
        age_group: "",
        location: "",
      },
      injurySearchCriteria: {
        age_group: "",
        location: "",
      },
      results: [],
      errorMessage: "",
      isNoResults: false,
      isDeathSearch: false, // Tracks if the search is for deaths or injuries
    };
  },
  methods: {
    async searchDeaths() {
      this.isDeathSearch = true; // Set flag for deaths
      await this.fetchData("https://fit5120ta19.onrender.com/DrowningDeathSearch", this.deathSearchCriteria);

    },
    async searchInjuries() {
      this.isDeathSearch = false; // Set flag for injuries
      await this.fetchData("https://fit5120ta19.onrender.com/DrowningInjurySearch", this.injurySearchCriteria);
    },
    async fetchData(endpoint, criteria) {
      try {
        this.errorMessage = "";
        const response = await axios.get(endpoint, { params: criteria });

        console.log("API Response:", response.data); // Debugging: Check if 'rates' exists in response

        if (response.data.length === 0) {
          this.isNoResults = true;
        } else {
          this.isNoResults = false;
        }

        // Process results to ensure 'rate' is correctly mapped
        this.results = response.data.map(item => ({
          location: item.location,
          age_group: item.age_group,
          deaths: item.deaths,
          cases: item.cases,
          rate: item.rate !== null ? parseFloat(item.rate) : null // Ensure rate is always a number
        }));

      } catch (error) {
        console.error("Error fetching data:", error.response || error.message);
        this.errorMessage = "An error occurred while fetching data. Please try again later.";
      }
    },
    clearFilters() {
      this.deathSearchCriteria = { age_group: "", location: "" };
      this.injurySearchCriteria = { age_group: "", location: "" };
      this.results = [];
      this.isNoResults = false;
      this.errorMessage = "";
      this.isDeathSearch = false; // Reset flag
    },
  },
};
</script>

<style scoped>
.error-message {
  color: red;
  font-weight: bold;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

h2, h3 {
  margin-top: 20px;
}
</style>