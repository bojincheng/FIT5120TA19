<template>
  <div class="custom-chart-container">
    <h3 class="chart-title">{{ chartData.datasets[0].label }} vs {{ chartData.datasets[1].label }}</h3>
    
    <!-- Safety Insights for Immigrant Families -->
    <div class="safety-insights-container">
      <h3 class="insights-title">What This Means For Your Family</h3>
      <p class="insights-subtitle">Understanding these conditions can help keep your family safe at Australian beaches</p>
      
      <div class="safety-comparison">
        <div v-for="(dataset, i) in chartData.datasets" :key="i" class="beach-safety-column">
          <div class="beach-type-label">{{ i === 0 ? 'Home Beach' : 'New Beach' }}</div>
          <h4 class="beach-safety-name">{{ dataset.label }} Safety Assessment</h4>
          
          <!-- Overall Beach Condition Category -->
          <div class="condition-category" :class="getConditionCategoryClass(dataset.data)">
            <span class="category-label">{{ getBeachConditionCategory(dataset.data) }}</span>
            <p class="category-description">{{ getBeachConditionDescription(dataset.data) }}</p>
          </div>
          
          <!-- Rip Current Risk -->
          <div class="safety-factor">
            <div class="factor-header">
              <span class="factor-icon">🌀</span>
              <span class="factor-title">Rip Current Risk</span>
              <span :class="getRiskClass(getRipCurrentRisk(dataset.data[4]))">{{ getRipCurrentRisk(dataset.data[4]) }}</span>
            </div>
            <p class="factor-explanation">{{ getRipCurrentExplanation(dataset.data[4]) }}</p>
          </div>
          
          <!-- Wave Danger -->
          <div class="safety-factor">
            <div class="factor-header">
              <span class="factor-icon">🌊</span>
              <span class="factor-title">Wave Danger</span>
              <span :class="getRiskClass(getWaveDanger(dataset.data[2], dataset.data[3]))">{{ getWaveDanger(dataset.data[2], dataset.data[3]) }}</span>
            </div>
            <p class="factor-explanation">{{ getWaveExplanation(dataset.data[2], dataset.data[3]) }}</p>
          </div>
          
          <!-- Water Fatigue -->
          <div class="safety-factor">
            <div class="factor-header">
              <span class="factor-icon">🌡️</span>
              <span class="factor-title">Water Fatigue</span>
              <span :class="getRiskClass(getWaterFatigue(dataset.data[5]))">{{ getWaterFatigue(dataset.data[5]) }}</span>
            </div>
            <p class="factor-explanation">{{ getWaterFatigueExplanation(dataset.data[5]) }}</p>
          </div>
          
          <!-- Visibility & Control -->
          <div class="safety-factor">
            <div class="factor-header">
              <span class="factor-icon">⚠️</span>
              <span class="factor-title">Visibility & Control</span>
              <span :class="getRiskClass(getVisibilityControl(dataset.data[1]))">{{ getVisibilityControl(dataset.data[1]) }}</span>
            </div>
            <p class="factor-explanation">{{ getVisibilityExplanation(dataset.data[1]) }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BarChart',
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartTitle: {
      type: String,
      default: 'Beach Safety Comparison'
    }
  },
  methods: {
    // Beach condition categorization
    getBeachConditionCategory(data) {
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const swellHeight = data[3] || 0;
      const windSpeed = data[1] || 0;
      
      // Calculate effective wave height
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      // Count high-risk factors
      let highRiskFactors = 0;
      if (currentSpeed > 0.5) highRiskFactors++;
      if (effectiveHeight > 1.2) highRiskFactors++;
      if (windSpeed > 25) highRiskFactors++;
      
      // Count moderate risk factors
      let moderateRiskFactors = 0;
      if (currentSpeed > 0.3 && currentSpeed <= 0.5) moderateRiskFactors++;
      if (effectiveHeight > 0.7 && effectiveHeight <= 1.2) moderateRiskFactors++;
      if (windSpeed > 15 && windSpeed <= 25) moderateRiskFactors++;
      
      // Categorize based on risk factors
      if (highRiskFactors >= 1) {
        return "Harsh Conditions";
      } else if (moderateRiskFactors >= 2 || (moderateRiskFactors >= 1 && currentSpeed > 0.3)) {
        return "Moderate Conditions";
      } else {
        return "Calm Conditions";
      }
    },
    
    getConditionCategoryClass(data) {
      const category = this.getBeachConditionCategory(data);
      if (category.includes("Harsh")) return "category-harsh";
      if (category.includes("Moderate")) return "category-moderate";
      return "category-calm";
    },
    
    getBeachConditionDescription(data) {
      const category = this.getBeachConditionCategory(data);
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const swellHeight = data[3] || 0;
      
      if (category.includes("Harsh")) {
        return `Challenging beach conditions with ${currentSpeed > 0.5 ? 'strong currents' : 'high waves'}. Not suitable for inexperienced swimmers or children.`;
      } else if (category.includes("Moderate")) {
        return `Exercise caution in these medium-intensity conditions. Suitable for capable swimmers, but supervise children closely.`;
      } else {
        return `Relatively gentle beach conditions with lower risk.`;
      }
    },
    
    // Safety assessment methods
    getRiskClass(risk) {
      if (risk === 'High') return 'risk-high';
      if (risk === 'Moderate') return 'risk-moderate';
      if (risk === 'Low') return 'risk-low';
      return '';
    },
    
    // Rip Current Risk
    getRipCurrentRisk(currentSpeed) {
      if (currentSpeed > 0.5) return 'High';
      if (currentSpeed > 0.3) return 'Moderate';
      return 'Low';
    },
    
    getRipCurrentExplanation(currentSpeed) {
      if (currentSpeed > 0.5) {
        return `High chance of rip currents. The strong current (${currentSpeed.toFixed(2)} m/s) creates powerful rips that can pull even adults 50-100 meters offshore in minutes. Children will be pulled out instantly, with little chance to react.`;
      } else if (currentSpeed > 0.3) {
        return `Moderate chance of rip currents forming. These currents (${currentSpeed.toFixed(2)} m/s) can pull children 20-30 meters offshore quickly. Adults may struggle to swim against these rips.`;
      } else {
        return `Lower chance of rip currents forming, but they can still develop. Current speed (${currentSpeed.toFixed(2)} m/s) means if caught in a rip, you'd be pulled about 5-10 meters offshore. Watch for darker patches of water and less breaking waves.`;
      }
    },
    
    // Wave Danger
    getWaveDanger(waveHeight, swellHeight) {
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      if (effectiveHeight > 1.2) return 'High';
      if (effectiveHeight > 0.7) return 'Moderate';
      return 'Low';
    },
    
    getWaveExplanation(waveHeight, swellHeight) {
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      if (effectiveHeight > 1.2) {
        return `Strong waves (${effectiveHeight.toFixed(2)} m) can knock down adults and children. Not safe for play or swimming today, especially for children.`;
      } else if (effectiveHeight > 0.7) {
        return `These waves (${effectiveHeight.toFixed(2)} m) can be challenging for children and inexperienced swimmers. Keep children in shallow water only.`;
      } else {
        return `Gentler waves (${effectiveHeight.toFixed(2)} m) are better for swimming, but always supervise children closely.`;
      }
    },
    
    // Water Fatigue
    getWaterFatigue(waterTemp) {
      if (waterTemp < 18) return 'High';
      if (waterTemp < 22) return 'Moderate';
      return 'Low';
    },
    
    getWaterFatigueExplanation(waterTemp) {
      if (waterTemp < 18) {
        return `Cold water (${waterTemp.toFixed(1)}°C) causes fatigue much faster. Children will tire quickly, increasing drowning risk. Take short dips only.`;
      } else if (waterTemp < 22) {
        return `Cool water (${waterTemp.toFixed(1)}°C) causes moderate fatigue. Take regular breaks from swimming and watch for shivering in children.`;
      } else {
        return `More comfortable water temperature (${waterTemp.toFixed(1)}°C), but still monitor children for signs of fatigue.`;
      }
    },
    
    // Visibility & Control
    getVisibilityControl(windSpeed) {
      if (windSpeed > 25) return 'High Risk';
      if (windSpeed > 15) return 'Moderate Risk';
      return 'Better Conditions';
    },
    
    getVisibilityExplanation(windSpeed) {
      if (windSpeed > 25) {
        return `Very windy conditions (${windSpeed.toFixed(1)} km/h) create choppy water. Hard to see or hear your child if they struggle. Stay extremely close to children or consider a different activity today.`;
      } else if (windSpeed > 15) {
        return `Moderately windy (${windSpeed.toFixed(1)} km/h) conditions affect visibility and ability to hear calls for help. Keep children within arm's reach at all times.`;
      } else {
        return `Calmer conditions (${windSpeed.toFixed(1)} km/h) make it easier to monitor children in the water.`;
      }
    }
  }
};
</script>

<style scoped>
.custom-chart-container {
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1.5rem;
  background-color: #f8fafc;
  height: 100%;
  width: 100%;
}

.chart-title {
  text-align: center;
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
  font-weight: bold;
  color: #334155;
}

/* Safety Insights Styles */
.safety-insights-container {
  padding-top: 0.5rem;
}

.insights-title {
  text-align: center;
  font-size: 1.5rem;
  font-weight: bold;
  color: #1e3a8a;
  margin-bottom: 0.5rem;
}

.insights-subtitle {
  text-align: center;
  color: #64748b;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.safety-comparison {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.beach-safety-column {
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  padding: 1rem;
  background-color: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.beach-safety-name {
  text-align: center;
  font-weight: 600;
  padding-bottom: 0.75rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid #e2e8f0;
  color: #1e40af;
}

.safety-factor {
  margin-bottom: 1.25rem;
  padding-bottom: 1rem;
  border-bottom: 1px dashed #e2e8f0;
}

.safety-factor:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.factor-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.factor-icon {
  font-size: 1.25rem;
  margin-right: 0.5rem;
}

.factor-title {
  font-weight: 600;
  color: #334155;
  flex: 1;
}

.risk-high {
  background-color: #fee2e2;
  color: #b91c1c;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.risk-moderate {
  background-color: #fef3c7;
  color: #b45309;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.risk-low {
  background-color: #dcfce7;
  color: #15803d;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.875rem;
}

.factor-explanation {
  margin: 0;
  color: #4b5563;
  font-size: 0.95rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .safety-comparison {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .safety-factor {
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
  }
  
  .factor-explanation {
    font-size: 0.9rem;
  }
}

@media (max-width: 640px) {
  .custom-chart-container {
    padding: 1rem;
  }
  
  .insights-title {
    font-size: 1.25rem;
  }
  
  .factor-header {
    flex-wrap: wrap;
  }
  
  .factor-title {
    margin-right: 0.5rem;
  }
}

.condition-category {
  margin-bottom: 1.5rem;
  padding: 0.75rem;
  border-radius: 0.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding-left: 10%;
}

.category-harsh {
  background-color: #fee2e2;
  border: 1px solid #ef4444;
  margin-left: auto;
  margin-right: auto;
}

.category-moderate {
  background-color: #fef3c7;
  border: 1px solid #f59e0b;
  margin-left: auto;
  margin-right: auto;
}

.category-calm {
  background-color: #dcfce7;
  border: 1px solid #10b981;
  margin-left: auto;
  margin-right: auto;
}

.category-label {
  font-size: 1.1rem;
  font-weight: 700;
  display: block;
  margin-bottom: 0.5rem;
  text-align: center;
  margin-left: 10%;
}

.category-harsh .category-label {
  color: #b91c1c;
}

.category-moderate .category-label {
  color: #b45309;
}

.category-calm .category-label {
  color: #15803d;
}

.category-description {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.beach-type-label {
  background-color: #2563eb;
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 0.5rem;
  text-align: center;
  margin: 0 auto 1rem;
  font-size: 0.9rem;
  display: inline-block;
  font-weight: 600;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style> 