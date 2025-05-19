<template>
  <div class="drowning-search">
    <div class="intro-banner">
      <h2>Protecting Our Little Ones</h2>
      <p>
        Every drowning case is a heartbreaking loss — especially for families new to Australia, where water safety rules and risks may be unfamiliar. This tool helps you understand where, how, and to whom drowning happens — so we can prevent it together.
      </p>
    </div>

    <!-- Key Statistics Section -->
    <div class="key-statistics">
      <h2>Key Drowning Statistics</h2>
      <div class="statistics-grid">
        <div class="statistic-card">
          <h3>Children 0-4 years</h3>
          <div class="large-percentage">{{ poolDrowningStats.age0to4Percentage }}%</div>
          <p>of drowning deaths in this age group occur in swimming pools</p>
        </div>
        <div class="statistic-card">
          <h3>Children 5-14 years</h3>
          <div class="large-percentage">{{ poolDrowningStats.age5to14Percentage }}%</div>
          <p>of drowning deaths in this age group occur in swimming pools</p>
        </div>
        <div class="statistic-card">
          <h3>Teenagers 15-24 years</h3>
          <div class="large-percentage">{{ teenFreshwaterStats.percentage }}%</div>
          <p>of drowning deaths in teenagers occur in natural water</p>
        </div>
      </div>
    </div>

    <h1>Drowning Statistics Search</h1>

    <!-- Drowning Deaths Search Section -->
    <h2>Search Drowning Deaths</h2>
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

    <!-- Drowning Injuries Search Section -->
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
            <th>Cases</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(result, index) in results"
            :key="index"
            @click="showVisual(result)"
          >
            <td>{{ result.location }}</td>
            <td>{{ result.age_group || "All age groups" }}</td>
            <td>
              <span v-if="isDeathSearch">{{ result.deaths }} deaths</span>
              <span v-else>{{ result.cases }} cases</span>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pop-up for Visualisation -->
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <span @click="closePopup" class="close-btn">&times;</span>
          <h4>
            {{ isDeathSearch ? "Understanding Drowning Deaths" : "Understanding Drowning Injuries" }}
          </h4>
          <p>For age group {{ selectedResult.age_group || "All" }} at {{ selectedResult.location }}:</p>
          <div class="visuals">
            <div
              v-for="i in (isDeathSearch ? selectedResult.deaths : selectedResult.cases)"
              :key="i"
              class="visual-child"
            >
              <span v-if="selectedResult.age_group === '0-4'">👶</span>
              <span v-else-if="i % 2 === 0">👦</span>
              <span v-else>👧</span>
            </div>
          </div>
          <p>
            This represents
            {{ isDeathSearch ? selectedResult.deaths : selectedResult.cases }}
            {{ isDeathSearch ? "drowning deaths" : "drowning injury cases" }} — each icon stands for a real child whose life was 
            lost or forever changed. As parents, it's painful to imagine, but vital to acknowledge: behind every symbol is a son, 
            a daughter, a story that ended or changed too soon. We use icons, not photos, to honor privacy and dignity — but the reality they represent is heartbreakingly real.
          </p>
        </div>
      </div>
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
      isDeathSearch: false,
      showPopup: false,
      selectedResult: {},
      poolDrowningStats: {
        age0to4Percentage: 0,
        age5to14Percentage: 0
      },
      teenFreshwaterStats: {
        percentage: 0
      }
    };
  },
  created() {
    const percentages = this.calculatePoolDrowningPercentages();
    this.poolDrowningStats.age0to4Percentage = percentages.age0to4Percentage;
    this.poolDrowningStats.age5to14Percentage = percentages.age5to14Percentage;
    
    const teenStats = this.calculateTeenFreshwaterDrowningPercentage();
    this.teenFreshwaterStats.percentage = teenStats.percentage;
  },
  methods: {
    async searchDeaths() {
      this.isDeathSearch = true;
      await this.fetchData("https://fit5120ta19.onrender.com/DrowningDeathSearch", this.deathSearchCriteria);
    },
    async searchInjuries() {
      this.isDeathSearch = false;
      await this.fetchData("https://fit5120ta19.onrender.com/DrowningInjurySearch", this.injurySearchCriteria);
    },
    calculateTeenFreshwaterDrowningPercentage() {
      /* 
      This method calculates the percentage of freshwater (natural water) drownings for teenagers (15-24 years)
      using data from the drowning_deaths table.
      
      Raw data from the database:
      - Age 15-24 years:
        * Natural water drownings: 21 deaths
        * Total drownings in age group: 30 deaths
      */
      
      // Raw data values
      const data = {
        age15to24: {
          naturalWaterDeaths: 21,
          totalDeaths: 30,
          exactPercentage: (21/30) * 100, // 70.00%
          roundedPercentage: 70 // Already at a round number
        }
      };
      
      // Print-ready formatted strings
      const printFormat = {
        age15to24: {
          statistic: `${data.age15to24.roundedPercentage}%`,
          detailedStatistic: `${data.age15to24.naturalWaterDeaths} out of ${data.age15to24.totalDeaths} drowning deaths (${data.age15to24.exactPercentage.toFixed(1)}%)`,
          description: `of drowning deaths in teenagers aged 15-24 years occur in natural water`,
          fullSentence: `${data.age15to24.roundedPercentage}% of drowning deaths in teenagers aged 15-24 years occur in natural water (${data.age15to24.naturalWaterDeaths} out of ${data.age15to24.totalDeaths} deaths).`
        }
      };
      
      return {
        // Value for display
        percentage: data.age15to24.roundedPercentage,
        
        // Raw data for calculations
        rawData: data,
        
        // Formatted text for printing
        printFormat: printFormat
      };
    },
    calculatePoolDrowningPercentages() {
      /* 
      This method calculates the percentage of pool drownings for young age groups
      using data from the drowning_deaths table.
      
      Raw data from the database:
      - Age 0-4 years:
        * Swimming pool drownings: 7 deaths
        * Total drownings in age group: 18 deaths
        
      - Age 5-14 years:
        * Swimming pool drownings: 3 deaths
        * Total drownings in age group: 12 deaths
      */
      
      // Raw data values
      const data = {
        age0to4: {
          poolDeaths: 7,
          totalDeaths: 18,
          exactPercentage: (7/18) * 100, // 38.89%
          roundedPercentage: 40, // Rounded to nearest 5%
        },
        age5to14: {
          poolDeaths: 3, 
          totalDeaths: 12,
          exactPercentage: (3/12) * 100, // 25.00%
          roundedPercentage: 25, // Already at a 5% increment
        }
      };
      
      // Print-ready formatted strings
      const printFormat = {
        age0to4: {
          statistic: `${data.age0to4.roundedPercentage}%`,
          detailedStatistic: `${data.age0to4.poolDeaths} out of ${data.age0to4.totalDeaths} drowning deaths (${data.age0to4.exactPercentage.toFixed(1)}%)`,
          description: `of drowning deaths in children aged 0-4 years occur in swimming pools`,
          fullSentence: `${data.age0to4.roundedPercentage}% of drowning deaths in children aged 0-4 years occur in swimming pools (${data.age0to4.poolDeaths} out of ${data.age0to4.totalDeaths} deaths).`
        },
        age5to14: {
          statistic: `${data.age5to14.roundedPercentage}%`,
          detailedStatistic: `${data.age5to14.poolDeaths} out of ${data.age5to14.totalDeaths} drowning deaths (${data.age5to14.exactPercentage.toFixed(1)}%)`,
          description: `of drowning deaths in children aged 5-14 years occur in swimming pools`,
          fullSentence: `${data.age5to14.roundedPercentage}% of drowning deaths in children aged 5-14 years occur in swimming pools (${data.age5to14.poolDeaths} out of ${data.age5to14.totalDeaths} deaths).`
        }
      };
      
      return {
        // Values for display
        age0to4Percentage: data.age0to4.roundedPercentage,
        age5to14Percentage: data.age5to14.roundedPercentage,
        
        // Raw data for calculations
        rawData: data,
        
        // Formatted text for printing
        printFormat: printFormat
      };
    },
    async fetchData(endpoint, criteria) {
      try {
        this.errorMessage = "";
        const response = await axios.get(endpoint, { params: criteria });

        if (response.data.length === 0) {
          this.isNoResults = true;
        } else {
          this.isNoResults = false;
        }

        this.results = response.data.map(item => ({
          location: item.location,
          age_group: item.age_group,
          deaths: item.deaths,
          cases: item.cases,
        }));
      } catch (error) {
        this.errorMessage = "An error occurred while fetching data. Please try again later.";
        console.error("Fetch error:", error.response || error.message);
      }
    },
    clearFilters() {
      this.deathSearchCriteria = { age_group: "", location: "" };
      this.injurySearchCriteria = { age_group: "", location: "" };
      this.results = [];
      this.isNoResults = false;
      this.errorMessage = "";
      this.isDeathSearch = false;
    },
    showVisual(result) {
      const count = this.isDeathSearch ? result.deaths : result.cases;
      if (count > 0) {
        this.selectedResult = result;
        this.showPopup = true;
      }
    },
    closePopup() {
      this.showPopup = false;
    },
  },
};
</script>

<style scoped>
.drowning-search {
  background-color: #f9fdfd;
  padding: 20px;
  font-family: 'Segoe UI', sans-serif;
  color: #333;
}

.intro-banner {
  background-color: #e0f7fa;
  padding: 15px;
  margin-bottom: 20px;
  border-left: 5px solid #0097a7;
  border-radius: 4px;
}

.intro-banner h2 {
  margin-top: 0;
  color: #007c91;
}

.intro-banner p {
  margin: 0;
  font-size: 1.1em;
  color: #444;
}

.error-message {
  color: red;
  font-weight: bold;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  background-color: #fff;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

th {
  background-color: #dfeef3;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.popup-content {
  background-color: white;
  padding: 25px;
  border-radius: 6px;
  width: 80%;
  max-width: 800px;
  overflow-y: auto;
  position: relative;
}

.close-btn {
  font-size: 24px;
  font-weight: bold;
  color: #aaa;
  cursor: pointer;
  position: absolute;
  top: 5px;
  right: 10px;
}

.visuals {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
  padding: 10px 0;
  max-height: 300px;
  overflow-y: auto;
}

.visual-child {
  font-size: 24px;
  flex-shrink: 0;
}

.rate-note {
  font-size: 0.9em;
  color: #555;
}

.key-statistics {
  background-color: #f0f7fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.statistics-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 15px;
}

.statistic-card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  flex: 1;
  min-width: 250px;
  border-left: 5px solid #0097a7;
}

.statistic-card h3 {
  margin-top: 0;
  color: #007c91;
  font-size: 1.2em;
}

.large-percentage {
  font-size: 3.5em;
  font-weight: bold;
  color: #e74c3c;
  margin: 10px 0;
}

.statistic-card p {
  margin: 0;
  color: #444;
  font-weight: 500;
}

/* Add responsiveness for mobile */
@media (max-width: 768px) {
  .statistics-grid {
    flex-direction: column;
  }
  
  .statistic-card {
    min-width: auto;
  }
}
</style>




