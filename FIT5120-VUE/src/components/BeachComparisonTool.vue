<template>
  <div class="beach-search-container">
    <div class="tab-buttons">
      <button @click="activeTab = 'ripIdentifier'" :class="['tab-button', activeTab === 'ripIdentifier' ? 'active' : '']">RIP IDENTIFIER</button>
      <button @click="activeTab = 'search'" :class="['tab-button', activeTab === 'search' ? 'active' : '']">SEARCH BEACHES</button>
      <button @click="activeTab = 'compare'" :class="['tab-button', activeTab === 'compare' ? 'active' : '']">COMPARE BEACHES</button>
    </div>
    
    <!-- Add the new Rip Identifier tab content -->
    <div v-if="activeTab === 'ripIdentifier'" class="ripIdentifier-tab">
      <div class="option-header">
        <h3 class="option-title">IDENTIFY RIP CURRENTS</h3>
      </div>
      
      <div class="rip-upload-container">
        <div class="upload-area" @click="triggerRipFileUpload" :class="{ 'has-image': ripImage }">
          <input type="file" ref="ripFileInput" class="hidden-file-input" accept="image/*" @change="handleRipImageUpload" />
          <div v-if="!ripImage" class="upload-placeholder">
            <div class="upload-icon">📷</div>
            <p>Click to upload a beach photo</p>
            <span class="upload-hint">or drag and drop image here</span>
          </div>
          <img v-if="ripImage" :src="ripImage" alt="Beach image" class="uploaded-image" />
        </div>
        
        <div class="rip-actions" v-if="ripImage">
          <button class="analyze-rip-button" @click="analyzeRipImage" :disabled="analyzeRipLoading">
            <span v-if="!analyzeRipLoading">Analyze for Rips</span>
            <div v-else class="button-loader"></div>
          </button>
          <button class="remove-image-button" @click="removeRipImage">
            <span>Remove Image</span>
          </button>
        </div>
        
        <div v-if="analyzeRipLoading" class="analyzing-message">
          <div class="loading-spinner"></div>
          <p>Analyzing beach image for rip currents...</p>
        </div>
        
        <div v-if="ripAnalysisResult" class="rip-analysis-result">
          <h4 class="result-title">Analysis Results</h4>
          
          <div class="result-image-container">
            <img :src="ripAnalysisResult.markedImage || ripImage" class="result-image" alt="Analysis result" />
            <div class="result-overlay" :class="ripAnalysisResult.dangerLevel">
              <span class="danger-badge">{{ ripAnalysisResult.dangerText }}</span>
            </div>
          </div>
          
          <div class="result-details">
            <div class="danger-indicator" :class="ripAnalysisResult.dangerLevel">
              <span class="danger-level">{{ ripAnalysisResult.dangerText }}</span>
              <div class="danger-bar-container">
                <div class="danger-bar" :style="{ width: ripAnalysisResult.dangerPercentage + '%' }"></div>
              </div>
            </div>
            
            <div class="result-description">
              <p>{{ ripAnalysisResult.description }}</p>
            </div>
            
            <div class="safety-tips">
              <h5>Safety Tips:</h5>
              <ul>
                <li v-for="(tip, index) in ripAnalysisResult.safetyTips" :key="index">{{ tip }}</li>
              </ul>
            </div>
          </div>
        </div>
        

      </div>
    </div>
    
          <div v-if="activeTab === 'search'" class="search-tab">
      <div class="option-header">
        <h3 class="option-title">CHECK BEACH CONDITIONS</h3>
        <p class="option-description">Enter the name of any Australian beach to see:</p>
      </div>
      
      <div class="search-input-container">
        <input
          v-model="address"
          @input="debouncedSearch"
          placeholder="Search for a beach (e.g. Bondi Beach)"
          class="search-input"
          ref="searchInput"
        />
      </div>
      
      <!-- Add spacing div that grows when suggestions are shown -->
      <div :style="{ height: suggestions.length ? '200px' : '0', transition: 'height 0.3s ease' }" class="suggestion-spacing"></div>
      
      <div v-if="loading" class="loading-message">
        <div class="loading-spinner"></div>
        <p>Loading real-time beach data...</p>
        <p class="loading-details">This may take up to 30 seconds as we retrieve current weather and marine conditions</p>
      </div>
      <div v-if="error" class="error-message">
        <div>{{ error }}</div>
        <button 
          @click="retrySearch()" 
          style="margin-top: 0.75rem; background: #e74c3c; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;"
        >
          Retry
        </button>
      </div>
      
      <!-- Success message displayed after search while popup is shown -->
      <div v-if="weather?.current && marine" class="search-success-message">
        <div class="success-indicator">
          <span class="success-icon">✓</span>
          <span class="success-text">Beach data loaded successfully</span>
        </div>
      </div>
    </div>
    
          <div v-else-if="activeTab === 'compare'" class="compare-tab">
        <div class="option-header">
          <h3 class="option-title">COMPARE BEACHES CONDITIONS</h3>
          <p class="option-description">Compare Australian beaches with beaches from home</p>
        </div>
      
              <div class="compare-wrapper" :class="{ 'expanded': suggestions1.length || suggestions2.length }">
        <div class="compare-inputs">
          <!-- Top row with both inputs side by side -->
          <div class="compare-inputs-row">
            <div class="compare-input-wrapper">
              <div class="beach-label">Home Beach</div>
              <div class="compare-input-container">
                <div class="input-icon">🏖️</div>
                <input
                  v-model="compareAddress1"
                  @input="debouncedSearchCompare1"
                  placeholder="Enter home beach (e.g. Goa Beach)"
                  class="search-input"
                />
                <ul
                  v-if="suggestions1.length"
                  class="suggestions-list"
                >
                  <li
                    v-for="(item, index) in suggestions1"
                    :key="index"
                    @click="selectCompareSuggestion(item, 1)"
                    class="suggestion-item"
                  >
                    {{ item.display_name }}
                  </li>
                </ul>
              </div>
            </div>
        
            <div class="compare-input-wrapper">
              <div class="beach-label">New Beach</div>
              <div class="compare-input-container">
                <div class="input-icon">🏝️</div>
                <input
                  v-model="compareAddress2"
                  @input="debouncedSearchCompare2"
                  placeholder="Enter new beach (e.g. Bondi Beach)"
                  class="search-input"
                />
                <ul
                  v-if="suggestions2.length"
                  class="suggestions-list"
                >
                  <li
                    v-for="(item, index) in suggestions2"
                    :key="index"
                    @click="selectCompareSuggestion(item, 2)"
                    class="suggestion-item"
                  >
                    {{ item.display_name }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
          
          <!-- Bottom row with suggestions for both inputs -->
          <div class="suggestions-row" v-if="suggestions1.length || suggestions2.length">
            <div class="suggestions-column" :class="{ 'active': suggestions1.length }">
              <div 
                :style="{ 
                  height: suggestions1.length ? Math.min(250, suggestions1.length * 50) + 'px' : '0', 
                  opacity: suggestions1.length ? 1 : 0,
                  transition: 'all 0.4s ease-in-out'
                }" 
                class="suggestion-spacing"
              >
                <div v-if="suggestions1.length" class="suggestion-indicator">
                  <span>{{ suggestions1.length }} beaches found</span>
                </div>
              </div>
            </div>
            
            <div class="suggestions-column" :class="{ 'active': suggestions2.length }">
              <div 
                :style="{ 
                  height: suggestions2.length ? Math.min(250, suggestions2.length * 50) + 'px' : '0', 
                  opacity: suggestions2.length ? 1 : 0,
                  transition: 'all 0.4s ease-in-out'
                }" 
                class="suggestion-spacing"
              >
                <div v-if="suggestions2.length" class="suggestion-indicator">
                  <span>{{ suggestions2.length }} beaches found</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Compare button container to ensure proper spacing -->
        <div class="compare-button-container" :class="{ 'has-suggestions': suggestions1.length || suggestions2.length }">
          <button
            @click="fetchCompareBeaches"
            :disabled="!selectedBeach1 || !selectedBeach2 || areSameBeaches()"
            class="compare-button"
          >
            <span>{{ loading ? 'Loading...' : 'Compare Beaches' }}</span>
            <svg v-if="!loading" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
        
        <!-- Add a warning message when same beaches are selected -->
        <div v-if="selectedBeach1 && selectedBeach2 && areSameBeaches()" class="same-beach-warning">
          <div>
            <span class="warning-icon">⚠️</span> You've selected the same beach twice
          </div>
          <p>Please select two different beaches to compare their conditions.</p>
        </div>
        
      <div v-if="error" class="error-message">
        <div>{{ error }}</div>
        <button 
            @click="fetchCompareBeaches()" 
          style="margin-top: 0.75rem; background: #e74c3c; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;"
        >
          Retry
        </button>
      </div>
      
        <div v-if="loading" class="loading-message">
          <div class="loading-spinner"></div>
          <p>Loading comparison data...</p>
          <p class="loading-details">This may take up to 30 seconds as we retrieve and analyze conditions at both beaches</p>
        </div>
        
        <!-- Show debug message when comparison was attempted but failed -->
        <div v-if="activeTab === 'compare' && !loading && !compareChartData && attemptedCompare && selectedBeach1 && selectedBeach2" class="debug-message">
          <div>Chart data not available. Try clicking Compare again.</div>
          <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; justify-content: center;">
            <button 
              @click="fetchCompareBeaches" 
              style="background: #3498db; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;"
            >
              Retry Compare
            </button>
            <button 
              @click="showDebug = true" 
              style="background: #2c3e50; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;"
            >
              Show Debug Info
            </button>
          </div>
        </div>
        
        <!-- Success message displayed after compare while popup is shown -->
      <div v-if="compareChartData" class="compare-success-message">
        <div class="success-indicator">
          <span class="success-icon">✓</span>
          <span class="success-text">Beach comparison data loaded successfully</span>
        </div>
        <!-- Beach report is now shown automatically -->
      </div>
            </div>
          </div>
        </div>
        
  <!-- Beach search suggestions popup in portal to ensure it's outside any scrollable containers -->
  <div v-if="activeTab === 'search' && suggestions.length" class="search-suggestions-popup-overlay">
    <div class="search-suggestions-popup" :style="suggestionPopupStyle">
      <ul class="suggestions-popup-list">
        <li
          v-for="(item, index) in suggestions"
          :key="index"
          @click="selectSuggestion(item)"
          class="suggestion-popup-item"
            >
          {{ item.display_name }}
        </li>
      </ul>
            </div>
            </div>
  
  <!-- Beach safety report popup - shows the full report in a modal overlay -->
  <div v-if="showBeachReport && weather?.current && marine" class="beach-report-popup-overlay">
    <div class="beach-report-popup">
      <div class="popup-header">
        <h3 class="report-title">Beach Safety Report for {{ address }}</h3>
        <button class="close-popup-btn" @click="showBeachReport = false">×</button>
          </div>
          
      <div class="safety-rating">
        <h4>Today's Safety Level</h4>
        <div :class="['rating-indicator', getSafetyRatingClass()]">
          <span class="rating-label">{{ getSafetyRating() }}</span>
        </div>
      </div>
      
      <div class="report-content">
        <!-- Removed tabs since we're only showing condition breakdown -->
        <!-- Section header removed -->
        <div class="condition-section">
            <div class="condition-breakdown">
              <div class="condition-item">
                <div class="condition-header">
                  <div class="condition-title">
                    <span class="condition-name">Wave Risk Level</span>
                  </div>
                </div>
                
                <div class="risk-meter-container">
                  <div class="risk-meter">
                    <div class="risk-segments">
                      <div class="risk-segment safe"></div>
                      <div class="risk-segment caution"></div>
                      <div class="risk-segment danger"></div>
                    </div>
                    <div class="risk-indicator" :style="{ left: getWaveRiskPosition() }">
                      <div class="risk-indicator-arrow"></div>
                    </div>
                  </div>
                  <div class="risk-labels">
                    <span class="risk-label safe">Safe</span>
                    <span class="risk-label caution">Caution</span>
                    <span class="risk-label danger">Dangerous</span>
                  </div>
                </div>
                
                <div class="condition-meaning">
                  <div class="wave-visual-card">
                    <img 
                      v-if="marine.wave_height > 1.2" 
                      src="../assets/highwaves.avif" 
                      alt="Dangerous waves" 
                      class="wave-image" 
                    />
                    <img 
                      v-else-if="marine.wave_height > 0.3" 
                      src="../assets/mod_waves.jpg" 
                      alt="Moderate waves" 
                      class="wave-image" 
                    />
                    <img 
                      v-else 
                      src="../assets/low_waves.jpeg" 
                      alt="Calm waves" 
                      class="wave-image" 
                    />
                    <div class="hover-overlay">
                      <div class="hover-prompt">👆 Hover for details</div>
                    </div>
                    <div class="wave-details-card">
                      <div class="wave-comparison">
                        <p>These waves are <span class="highlight">{{ Math.round(marine.wave_height/1.2) > 1 ? Math.round(marine.wave_height/1.2) + '× taller than' : 'about the same height as' }}</span> a {{ marine.wave_height >= 1 ? '10' : '6' }}-year-old child</p>
                        <p>Similar to <span class="highlight">{{ Math.round(marine.wave_height) > 2 ? 'a bus' : (Math.round(marine.wave_height) > 1.5 ? 'a car' : (Math.round(marine.wave_height) > 1 ? 'an adult' : 'a coffee table')) }}</span> in height</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="condition-item">
                <div class="condition-header">
                  <div class="condition-title">
                    <span class="condition-name">Current Risk Level</span>
                  </div>
                </div>
                
                <div class="risk-meter-container">
                  <div class="risk-meter">
                    <div class="risk-segments">
                      <div class="risk-segment safe"></div>
                      <div class="risk-segment caution"></div>
                      <div class="risk-segment danger"></div>
                  </div>
                    <div class="risk-indicator" :style="{ left: getCurrentRiskPosition() }">
                      <div class="risk-indicator-arrow"></div>
                  </div>
                </div>
                  <div class="risk-labels">
                    <span class="risk-label safe">Safe</span>
                    <span class="risk-label caution">Caution</span>
                    <span class="risk-label danger">Dangerous</span>
                </div>
              </div>
              
                <div class="condition-meaning">
                  <div class="current-visual-card">
                    <img 
                      v-if="marine.ocean_current_velocity > 0.8" 
                      :src="images.dangerousCurrent" 
                      alt="Dangerous current" 
                      class="current-image" 
                    />
                    <img 
                      v-else-if="marine.ocean_current_velocity > 0.5 && marine.ocean_current_velocity <= 0.8" 
                      :src="images.moderateCurrent" 
                      alt="Strong current" 
                      class="current-image" 
                    />
                    <img 
                      v-else-if="marine.ocean_current_velocity > 0.3 && marine.ocean_current_velocity <= 0.5" 
                      :src="images.moderateCurrent" 
                      alt="Moderate current" 
                      class="current-image" 
                    />
                    <img 
                      v-else 
                      :src="images.lowCurrent" 
                      alt="Mild current" 
                      class="current-image" 
                    />
                    <div class="hover-overlay">
                      <div class="hover-prompt">👆 Hover for details</div>
                    </div>
                    <div class="current-details-card">
                      <div class="current-comparison">
                        <p>This current is <span class="highlight">{{ Math.round(marine.ocean_current_velocity/0.3) > 1 ? Math.round(marine.ocean_current_velocity/0.3) + '× faster than' : 'about the same speed as' }}</span> a 10-year-old child can swim</p>
                        <p v-if="marine.ocean_current_velocity > 0.5">Can quickly pull swimmers offshore in seconds</p>
                        <p v-else>Take precautions to avoid being pulled offshore</p>
                      </div>
                    </div>
                  </div>
                </div>
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
  <!-- Beach comparison report popup - shows the full comparison in a modal overlay -->
  <div v-if="showCompareReport && compareChartData" class="beach-report-popup-overlay">
    <div class="beach-report-popup">
      <div class="popup-header">
        <h3 class="report-title">Beach Comparison: {{ compareChartData.datasets[0].label }} vs {{ compareChartData.datasets[1].label }}</h3>
        <button class="close-popup-btn" @click="showCompareReport = false">×</button>
        </div>
      
      <div class="report-content">
        
            <div class="comparison-conclusion">
              <div class="conclusion-horizontal">
                <h4 class="conclusion-title">Are you prepared for {{ compareChartData.datasets[1].label }}?</h4>
                <div class="readiness-status">{{ getReadinessAnswer() }}</div>
              </div>
            </div>
            
            <div class="beach-comparison-cards">
              <div v-for="(dataset, i) in compareChartData.datasets" :key="i" class="beach-comparison-card" :class="getBeachCategoryClass(dataset.data)">
                <!-- Beach Image -->
                <div class="beach-image-container">
                  <img 
                    v-if="getBeachConditionCategory(dataset.data) === 'HARSH'" 
                    src="../assets/harsh_beach.jpeg" 
                    alt="Harsh beach conditions" 
                    class="beach-condition-image"
                  />
                  <img 
                    v-else-if="getBeachConditionCategory(dataset.data) === 'MODERATE'" 
                    src="../assets/moderate.jpeg" 
                    alt="Moderate beach conditions" 
                    class="beach-condition-image"
                  />
                  <img 
                    v-else 
                    src="../assets/calm_beach.jpeg" 
                    alt="Calm beach conditions" 
                    class="beach-condition-image"
                  />
                  <div class="beach-type-ribbon">{{ i === 0 ? 'Home Beach' : 'New Beach' }}</div>
                    </div>
                
                <h4 class="beach-title">{{ dataset.label }} Safety Assessment</h4>
                
                <!-- Beach Condition Category -->
                <div class="beach-condition-category" :class="getBeachCategoryClass(dataset.data)">
                  <span class="category-badge">{{ getBeachConditionCategory(dataset.data) }}</span>
                </div>
                
                <!-- Visual Wave Height Reference (only show if both beaches have wave data) -->
                <div v-if="shouldShowVisualCard('wave')" class="compare-info-container">
                  <div class="compare-info-header">
                    <h4 class="compare-info-title">Wave Height: {{ getConditionTerm(dataset.data, 'wave') }}</h4>
                  </div>
                  <div class="compare-info-content">
                    <div class="compare-info-image-container">
                      <img 
                        v-if="Math.max(dataset.data[2] || 0, dataset.data[3] || 0) > 1.2" 
                        src="../assets/highwaves.avif" 
                        alt="Dangerous waves" 
                        class="compare-info-image" 
                      />
                      <img 
                        v-else-if="Math.max(dataset.data[2] || 0, dataset.data[3] || 0) > 0.3" 
                        src="../assets/mod_waves.jpg" 
                        alt="Moderate waves" 
                        class="compare-info-image" 
                      />
                      <img 
                        v-else 
                        src="../assets/low_waves.jpeg" 
                        alt="Calm waves" 
                        class="compare-info-image" 
                      />
                      <div class="compare-info-hover-trigger">
                        <div class="compare-info-hover-prompt">Hover for details</div>
                      </div>
                      <div class="compare-info-overlay">
                        <div class="compare-info-hover-details">
                          <p>These waves are <span class="compare-info-highlight">{{ Math.round(Math.max(dataset.data[2] || 0, dataset.data[3] || 0)/1.2) > 1 ? Math.round(Math.max(dataset.data[2] || 0, dataset.data[3] || 0)/1.2) + '× taller than' : 'about the same height as' }}</span> a {{ Math.max(dataset.data[2] || 0, dataset.data[3] || 0) >= 1 ? '10' : '6' }}-year-old child</p>
                          <p>Similar to <span class="compare-info-highlight">{{ Math.round(Math.max(dataset.data[2] || 0, dataset.data[3] || 0)) > 2 ? 'a bus' : (Math.round(Math.max(dataset.data[2] || 0, dataset.data[3] || 0)) > 1.5 ? 'a car' : (Math.round(Math.max(dataset.data[2] || 0, dataset.data[3] || 0)) > 1 ? 'an adult' : 'a coffee table')) }}</span> in height</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
            <!-- Current Strength Visual -->
                <div v-if="shouldShowVisualCard('current')" class="compare-info-container">
                  <div class="compare-info-header">
                    <h4 class="compare-info-title">Current Strength: {{ getConditionTerm(dataset.data, 'current') }}</h4>
                  </div>
                  <div class="compare-info-content">
                    <div class="compare-info-image-container">
                                          <img 
                      v-if="(dataset.data[4] || 0) > 0.8" 
                      :src="images.dangerousCurrent" 
                      alt="Dangerous current" 
                      class="compare-info-image" 
                    />
                    <img 
                      v-else-if="(dataset.data[4] || 0) > 0.5 && (dataset.data[4] || 0) <= 0.8" 
                      :src="images.moderateCurrent" 
                      alt="Strong current" 
                      class="compare-info-image" 
                    />
                    <img 
                      v-else-if="(dataset.data[4] || 0) > 0.3 && (dataset.data[4] || 0) <= 0.5" 
                      :src="images.moderateCurrent" 
                      alt="Moderate current" 
                      class="compare-info-image" 
                    />
                    <img 
                      v-else 
                      :src="images.lowCurrent" 
                      alt="Mild current" 
                      class="compare-info-image" 
                    />
                      <div v-if="(dataset.data[4] || 0) > 0" class="compare-info-hover-trigger">
                        <div class="compare-info-hover-prompt">Hover for details</div>
                      </div>
                      <div v-if="(dataset.data[4] || 0) > 0" class="compare-info-overlay">
                                                  <div class="compare-info-hover-details">
                            <p>This current is <span class="compare-info-highlight">{{ Math.round((dataset.data[4] || 0)/0.3) > 1 ? Math.round((dataset.data[4] || 0)/0.3) + '× faster than' : 'about the same speed as' }}</span> a 10-year-old child can swim</p>
                            <p>Pulls you <span class="compare-info-highlight">{{ Math.round((dataset.data[4] || 0)*10) }}m offshore</span> in 10 seconds</p>
                          </div>
                      </div>
                      <div v-else class="compare-info-static">
                        <p>No significant current detected</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Best For Groups -->
                <div class="best-for-groups-container">
                  <div class="recommendation-label">Suitable For:</div>
                  <div class="suitability-wrapper">
                    <div class="suitability-header">
                      <div class="suitability-header-age">Age Group</div>
                      <div class="suitability-header-safe">Safe?</div>
                    </div>
                    <div class="suitability-row">
                      <div class="suitability-age">👶 Children (under 8)</div>
                      <div class="suitability-safe" :class="getChildSafetyClass(dataset.data)">{{ getChildSafety(dataset.data) }}</div>
                    </div>
                    <div class="suitability-row">
                      <div class="suitability-age">🧒 Older Kids (8-14)</div>
                      <div class="suitability-safe" :class="getOlderChildSafetyClass(dataset.data)">{{ getOlderChildSafety(dataset.data) }}</div>
                    </div>
                  </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import images
import dangerousCurrentImage from '../assets/dangerous_current.JPG'
import moderateCurrentImage from '../assets/moderate_current.jpg'
import lowCurrentImage from '../assets/low_current.jpg'
import childWaveDangerImage from '../assets/child_wave_danger.jpg'
import childWaveModerateImage from '../assets/child_wave_moderate.jpg'
import childWaveSafeImage from '../assets/child_wave_safe.jpg'
import harshBeachImage from '../assets/harsh_beach.jpeg'
import calmBeachImage from '../assets/calm_beach.jpeg'
import moderateBeachImage from '../assets/moderate.jpeg'
import highwavesImage from '../assets/highwaves.avif'
import modWavesImage from '../assets/mod_waves.jpg'
import lowWavesImage from '../assets/low_waves.jpeg'

export default {
  name: 'BeachComparisonTool',
  props: {
    initialTab: {
      type: String,
      default: 'search'
    },
    initialSearchValue: {
      type: String,
      default: ''
    },
    initialHomeBeach: {
      type: String,
      default: ''
    },
    initialCompareBeach: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      // Add imported images to the data
      images: {
        dangerousCurrent: dangerousCurrentImage,
        moderateCurrent: moderateCurrentImage,
        lowCurrent: lowCurrentImage,
        childWaveDanger: childWaveDangerImage,
        childWaveModerate: childWaveModerateImage,
        childWaveSafe: childWaveSafeImage,
        harshBeach: harshBeachImage,
        calmBeach: calmBeachImage,
        moderateBeach: moderateBeachImage,
        highwaves: highwavesImage,
        modWaves: modWavesImage,
        lowWaves: lowWavesImage
      },
      // Set default active tab to ripIdentifier
      activeTab: 'ripIdentifier',
      address: '',
      suggestions: [],
      suggestionPopupStyle: {
        top: '0px',
        left: '0px',
        width: '300px',
        display: 'none'
      },
      showBeachReport: false,
      loading: false,
      error: null,
      weather: null,
      marine: null,
      compareAddress1: '',
      suggestions1: [],
      compareAddress2: '',
      suggestions2: [],
      selectedBeach1: null,
      selectedBeach2: null,
      compareWeather1: null,
      compareMarine1: null,
      compareWeather2: null,
      compareMarine2: null,
      compareChartData: null,
      compareBeach1Name: '',
      compareBeach2Name: '',
      attemptedCompare: false, // Flag to track if comparison was attempted
      showCompareReport: false, // Flag to control compare popup visibility
      // Rip Identifier tab data
      ripImage: null,
      analyzeRipLoading: false,
      ripAnalysisResult: null,
      weatherCodeMap: {
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
      }
    }
  },
  mounted() {
    // Add watcher for compareChartData
    this.$watch('compareChartData', (newVal) => {
      console.log('compareChartData changed:', newVal ? 'Data available' : 'No data');
      if (newVal) {
        console.log('Chart datasets:', newVal.datasets.length);
        console.log('Beach 1:', newVal.datasets[0].label);
        console.log('Beach 2:', newVal.datasets[1].label);
      }
    });
    
    // Add watcher for activeTab
    this.$watch('activeTab', (newVal) => {
      console.log('Active tab changed to:', newVal);
      // Hide popups when changing tabs
      this.suggestionPopupStyle.display = 'none';
      this.showBeachReport = false;
      this.showCompareReport = false;
    });
    
    // Add watcher for suggestions array to reposition popup when suggestions change
    this.$watch('suggestions', (newVal) => {
      if (newVal.length > 0 && this.activeTab === 'search') {
        this.positionSearchSuggestionsPopup();
      } else {
        this.suggestionPopupStyle.display = 'none';
      }
    });

    // Handle window resize to reposition popup
    window.addEventListener('resize', this.handleWindowResize);
    
    // Handle clicks outside the popup to close it
    document.addEventListener('click', this.handleOutsideClick);

    // Initialize with props if provided
    this.initializeFromProps();
  },
  
  beforeDestroy() {
    // Clean up event listeners
    window.removeEventListener('resize', this.handleWindowResize);
    document.removeEventListener('click', this.handleOutsideClick);
  },
  methods: {
    // Initialize component with props values
    initializeFromProps() {
      // Set active tab if provided
      if (this.initialTab) {
        if (this.initialTab === 'search' || this.initialTab === 'compare' || this.initialTab === 'ripIdentifier') {
          this.activeTab = this.initialTab;
        }
      }
      
      // Set search value if provided
      if (this.initialSearchValue) {
        this.address = this.initialSearchValue;
        // Trigger search if we have a value
        this.debouncedSearch();
      }
      
      // Set compare values if provided
      if (this.initialHomeBeach) {
        this.compareAddress1 = this.initialHomeBeach;
        this.debouncedSearchCompare1();
      }
      
      if (this.initialCompareBeach) {
        this.compareAddress2 = this.initialCompareBeach;
        this.debouncedSearchCompare2();
      }
      
      // If we have both beaches for comparison, trigger the compare
      if (this.initialHomeBeach && this.initialCompareBeach && this.activeTab === 'compare') {
        // Wait for debounced search to complete
        setTimeout(() => {
          if (this.selectedBeach1 && this.selectedBeach2) {
            this.fetchCompareBeaches();
          }
        }, 1000);
      }
    },
    
    // Rip Identifier Methods
    triggerRipFileUpload() {
      this.$refs.ripFileInput.click();
    },
    
    handleRipImageUpload(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.ripImage = e.target.result;
          this.ripAnalysisResult = null; // Clear previous results
        };
        reader.readAsDataURL(file);
      }
    },
    
    removeRipImage() {
      this.ripImage = null;
      this.ripAnalysisResult = null;
      this.$refs.ripFileInput.value = ''; // Reset file input
    },
    
    analyzeRipImage() {
      // Mock analysis - in a real implementation, this would call an API
      this.analyzeRipLoading = true;
      
      // Simulate API call with timeout
      setTimeout(() => {
        this.analyzeRipLoading = false;
        
        // Generate mock analysis result
        const randomValue = Math.random();
        let dangerLevel, dangerText, dangerPercentage, description, safetyTips;
        
        if (randomValue < 0.33) {
          dangerLevel = 'low';
          dangerText = 'Low Risk';
          dangerPercentage = 25;
          description = 'No clear signs of rip currents in this image. The water appears to have consistent wave patterns with no visible dark channels or disruptions.';
          safetyTips = [
            'Always swim between the red and yellow flags',
            'Stay in shallow water and keep watch on children',
            'Conditions can change quickly - check regularly'
          ];
        } else if (randomValue < 0.66) {
          dangerLevel = 'medium';
          dangerText = 'Medium Risk';
          dangerPercentage = 60;
          description = 'Possible rip current indicators visible. Note the darker patches of water and gaps in the breaking waves which may indicate rip currents.';
          safetyTips = [
            'Avoid swimming near darker water channels',
            'Stay in waist-deep water maximum',
            'Keep children within arm\'s reach at all times'
          ];
        } else {
          dangerLevel = 'high';
          dangerText = 'High Risk';
          dangerPercentage = 90;
          description = 'Strong indicators of rip currents present! Multiple dark channels visible between breaking waves, with water flowing outward from the shore.';
          safetyTips = [
            'Do not enter the water in these conditions',
            'Alert lifeguards if you spot someone in trouble',
            'If caught in a rip, float and signal for help'
          ];
        }
        
        this.ripAnalysisResult = {
          dangerLevel,
          dangerText,
          dangerPercentage,
          description,
          safetyTips,
          // In a real implementation, this would be a processed image
          markedImage: this.ripImage
        };
      }, 2000);
    },
    
    convertMsToKmh(speedMs) {
      if (speedMs === undefined || speedMs === null || isNaN(speedMs)) return 0;
      // Convert meters per second to kilometers per hour (1 m/s = 3.6 km/h)
      const result = speedMs * 3.6;
      return isNaN(result) ? 0 : result; // Double check for NaN after conversion
    },
    getSafetyRating() {
      if (!this.marine || !this.weather) return 'Unknown';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      const swellHeight = this.marine.swell_wave_height || 0;
      
      // Calculate effective wave height
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      // Align with getBeachConditionCategory thresholds for consistency
      if (currentVelocity > 0.5 || effectiveHeight > 1.2) {
        return '🔴 High Risk – Not Safe for Children';
      } else if (currentVelocity > 0.3 || effectiveHeight > 0.7) {
        return '🟠 Moderate Risk – Caution Required';
      } else {
        return '🟢 Lower Risk – Good for Families';
      }
    },
    
    getSafetyRatingClass() {
      if (!this.marine || !this.weather) return 'rating-unknown';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      const swellHeight = this.marine.swell_wave_height || 0;
      
      // Calculate effective wave height
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      // Align with getBeachConditionCategory thresholds for consistency
      if (currentVelocity > 0.5 || effectiveHeight > 1.2) {
        return 'rating-high';
      } else if (currentVelocity > 0.3 || effectiveHeight > 0.7) {
        return 'rating-moderate';
      } else {
        return 'rating-low';
      }
    },
    
    getSafetyDescription() {
      if (!this.marine || !this.weather) return '';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      const swellHeight = this.marine.swell_wave_height || 0;
      
      // Calculate effective wave height
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      // Align with getBeachConditionCategory thresholds for consistency
      if (currentVelocity > 0.5 || effectiveHeight > 1.2) {
        return 'Dangerous conditions - high waves and strong currents make swimming unsafe for children and inexperienced swimmers.';
      } else if (currentVelocity > 0.3 || effectiveHeight > 0.7) {
        return 'Exercise caution - conditions may be challenging for children and inexperienced swimmers. Stay between the flags.';
      } else {
        return 'Generally favorable conditions, but always supervise children and swim between the flags.';
      }
    },
    
    getChildSafety() {
      if (!this.marine || !this.weather) return '❓';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentSpeed = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 0.8 || currentSpeed > 0.5) {
        return '❌';
      } else if (waveHeight > 0.5 || currentSpeed > 0.3) {
        return '⚠️';
      } else {
        return '✅';
      }
    },
    
    getChildSafetyClass() {
      if (!this.marine || !this.weather) return '';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 0.8 || currentVelocity > 0.5) {
        return 'safety-not-safe';
      } else if (waveHeight > 0.5 || currentVelocity > 0.3) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },
    
    getOlderChildSafety() {
      if (!this.marine || !this.weather) return '❓';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 1.2 || currentVelocity > 0.8) {
        return '❌';
      } else if (waveHeight > 0.7 || currentVelocity > 0.5) {
        return '⚠️';
      } else {
        return '✅';
      }
    },
    
    getOlderChildSafetyClass() {
      if (!this.marine || !this.weather) return '';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 1.2 || currentVelocity > 0.8) {
        return 'safety-not-safe';
      } else if (waveHeight > 0.7 || currentVelocity > 0.5) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },
    
    getInexperiencedAdultSafety() {
      if (!this.marine || !this.weather) return '❓';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 1.5 || currentVelocity > 1) {
        return '❌';
      } else if (waveHeight > 1 || currentVelocity > 0.7) {
        return '⚠️';
      } else {
        return '✅';
      }
    },
    
    getInexperiencedAdultSafetyClass() {
      if (!this.marine || !this.weather) return '';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 1.5 || currentVelocity > 1) {
        return 'safety-not-safe';
      } else if (waveHeight > 1 || currentVelocity > 0.7) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },
    
    getExperiencedAdultSafety() {
      if (!this.marine || !this.weather) return '❓';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 2 || currentVelocity > 1.5) {
        return '⚠️';
      } else if (waveHeight > 1.2 || currentVelocity > 1) {
        return '⚠️';
      } else {
        return '✅';
      }
    },
    
    getExperiencedAdultSafetyClass() {
      if (!this.marine || !this.weather) return '';
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      if (waveHeight > 2 || currentVelocity > 1.5) {
        return 'safety-caution';
      } else if (waveHeight > 1.2 || currentVelocity > 1) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },
    
    getKeyAdvice() {
      if (!this.marine || !this.weather) return [];
      
      const waveHeight = this.marine.wave_height || 0;
      const currentVelocity = this.marine.ocean_current_velocity || 0;
      
      let advice = [
        'Keep children close to shore within reach'
      ];
      
      if (waveHeight > 1 || currentVelocity > 0.8) {
        advice.push('Watch for rip currents - look for darker patches of water with fewer breaking waves.');
        advice.push('If caught in a rip, stay calm, float, and signal for help. Don\'t swim against the current.');
      }
      
      if (waveHeight > 1.5) {
        advice.push('If unsure, don\'t swim — paddle at the edge or visit a wave-protected beach instead.');
      }
      
      return advice;
    },
    async fetchCompareBeaches() {
      if (!this.selectedBeach1 || !this.selectedBeach2) {
        console.log('Missing beach selections - cannot compare');
        this.error = "Please select two beaches to compare";
        return;
      }
      
      // Check if user is trying to compare the same beach
      if (this.areSameBeaches()) {
        this.error = "Please select two different beaches to compare. You've selected the same beach twice.";
        return;
      }
      
      console.log('Compare button clicked, fetching data...');
      
      // Set the flag indicating comparison was attempted
      this.attemptedCompare = true;
      this.loading = true;
      this.error = null;
      
      // Clear any existing chart data to prevent stale displays
      this.compareChartData = null;
      this.compareBeach1Name = '';
      this.compareBeach2Name = '';
      
      try {
        // Make sure we're on compare tab
        this.activeTab = 'compare';
        
        const lat1 = parseFloat(this.selectedBeach1.lat);
        const lon1 = parseFloat(this.selectedBeach1.lon);
        const lat2 = parseFloat(this.selectedBeach2.lat);
        const lon2 = parseFloat(this.selectedBeach2.lon);
        
        // Set beach names
        this.compareBeach1Name = this.selectedBeach1.display_name.split(',')[0].trim();
        this.compareBeach2Name = this.selectedBeach2.display_name.split(',')[0].trim();
        
        console.log(`Fetching data for beach 1: ${this.compareBeach1Name} (${lat1}, ${lon1})`);
        
        // Fetch data for first beach
        let beach1Data;
        try {
          // Update loading status with specific beach info
          this.error = `Retrieving data for ${this.compareBeach1Name}...`;
          beach1Data = await this.fetchBeachData(lat1, lon1);
          console.log('Beach 1 data fetched successfully');
          this.error = null; // Clear status message
        } catch (error) {
          console.error('Error fetching beach 1 data:', error);
          throw new Error(`Failed to get data for ${this.compareBeach1Name}: ${error.message}`);
        }
        
        console.log(`Fetching data for beach 2: ${this.compareBeach2Name} (${lat2}, ${lon2})`);
        
        // Fetch data for second beach
        let beach2Data;
        try {
          // Update loading status with specific beach info
          this.error = `Retrieving data for ${this.compareBeach2Name}...`;
          beach2Data = await this.fetchBeachData(lat2, lon2);
          console.log('Beach 2 data fetched successfully');
          this.error = null; // Clear status message
        } catch (error) {
          console.error('Error fetching beach 2 data:', error);
          throw new Error(`Failed to get data for ${this.compareBeach2Name}: ${error.message}`);
        }
        
        // Update loading status again
        this.error = 'Creating comparison...';
        
        console.log('Both beaches data fetched successfully, creating comparison chart');
        
        // Delay for a moment to ensure smooth UI transition
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Create comparison chart data with safeguards for undefined/null values
        const beach1CurrentSpeed = beach1Data.marine.ocean_current_velocity !== undefined && 
                                  beach1Data.marine.ocean_current_velocity !== null ? 
                                  beach1Data.marine.ocean_current_velocity : 0;
        
        const beach2CurrentSpeed = beach2Data.marine.ocean_current_velocity !== undefined && 
                                  beach2Data.marine.ocean_current_velocity !== null ? 
                                  beach2Data.marine.ocean_current_velocity : 0;
        
        // Add detailed logging for comparison
        console.log('===== COMPARE BEACHES DATA =====');
        console.log(`Beach 1 (${this.compareBeach1Name}): Wave height: ${beach1Data.marine.wave_height} m, Current: ${beach1CurrentSpeed} m/s (${this.convertMsToKmh(beach1CurrentSpeed).toFixed(2)} km/h)`);
        console.log(`Beach 2 (${this.compareBeach2Name}): Wave height: ${beach2Data.marine.wave_height} m, Current: ${beach2CurrentSpeed} m/s (${this.convertMsToKmh(beach2CurrentSpeed).toFixed(2)} km/h)`);
        
        // Calculate and log beach 1 category
        const beach1DataArray = [
          0, // Temperature - not used for categorization 
          0, // Wind speed - not used for categorization anymore
          beach1Data.marine.wave_height || 0,
          beach1Data.marine.swell_wave_height || 0,
          beach1CurrentSpeed
        ];
        const beach1Category = this.getBeachConditionCategory(beach1DataArray);
        console.log(`Beach 1 (${this.compareBeach1Name}) category: ${beach1Category}`);
        
        // Calculate and log beach 2 category
        const beach2DataArray = [
          0, // Temperature - not used for categorization
          0, // Wind speed - not used for categorization anymore
          beach2Data.marine.wave_height || 0,
          beach2Data.marine.swell_wave_height || 0,
          beach2CurrentSpeed
        ];
        const beach2Category = this.getBeachConditionCategory(beach2DataArray);
        console.log(`Beach 2 (${this.compareBeach2Name}) category: ${beach2Category}`);
        console.log('==============================');
                                  
        this.compareChartData = {
          labels: [
            'Temperature (°C)', 
            'Wind Speed (km/h)', 
            'Wave Height (m)',
            'Swell Height (m)',
            'Current Speed (m/s)', // Display in m/s for consistency with calculations
          ],
          datasets: [
            {
              label: this.compareBeach1Name,
              backgroundColor: 'rgba(54, 162, 235, 0.7)',
                              data: [
                  beach1Data.weather.current.temperature_2m || 0,
                  beach1Data.weather.current.wind_speed_10m || 0,
                  beach1Data.marine.wave_height || 0,
                  beach1Data.marine.swell_wave_height || 0,
                  beach1CurrentSpeed, // Keep in m/s for getBeachConditionCategory
                ]
            },
            {
              label: this.compareBeach2Name,
              backgroundColor: 'rgba(255, 99, 132, 0.7)',
                              data: [
                  beach2Data.weather.current.temperature_2m || 0,
                  beach2Data.weather.current.wind_speed_10m || 0,
                  beach2Data.marine.wave_height || 0,
                  beach2Data.marine.swell_wave_height || 0,
                  beach2CurrentSpeed, // Keep in m/s for getBeachConditionCategory
                ]
            }
          ]
        };
        
        console.log('Comparison chart data created successfully');
        this.error = null; // Clear status message
        
        // Automatically show the comparison report when data is loaded
        // Set a slight delay to ensure all data is processed
        setTimeout(() => {
          this.showCompareReport = true;
        }, 300);
      } catch (error) {
        console.error('Compare beaches error:', error);
        this.error = `Failed to compare beaches: ${error.message}`;
      } finally {
        this.loading = false;
      }
    },
    async fetchBeachData(lat, lon) {
      console.log(`Fetching real beach data for coordinates (${lat}, ${lon})`);
      
      if (!lat || !lon || isNaN(lat) || isNaN(lon)) {
        console.error(`Invalid coordinates: (${lat}, ${lon})`);
        throw new Error('Invalid coordinates provided');
      }
      
      try {
        // API endpoints
        const weatherUrl = `https://fit5120ta19.onrender.com/weather?latitude=${lat}&longitude=${lon}`;
        const marineUrl = `https://fit5120ta19.onrender.com/marine?latitude=${lat}&longitude=${lon}`;
        
        console.log('Requesting weather data from:', weatherUrl);
        console.log('Requesting marine data from:', marineUrl);
        
        // Add timeout to API requests with increased timeout (60 seconds instead of 30)
        const fetchWithTimeout = (url, options = {}, timeout = 60000) => {
          return Promise.race([
            fetch(url, options),
            new Promise((_, reject) => 
              setTimeout(() => reject(new Error(`Request timed out after ${timeout}ms`)), timeout)
            )
          ]);
        };
        
        // Implementation of retry mechanism
        const fetchWithRetry = async (url, options = {}, maxRetries = 2) => {
          let lastError;
          
          for (let i = 0; i < maxRetries; i++) {
            try {
              const response = await fetchWithTimeout(url, options);
              if (!response.ok) {
                throw new Error(`HTTP error: ${response.status} - ${response.statusText}`);
              }
              return response;
            } catch (err) {
              console.warn(`Attempt ${i + 1} failed for ${url}: ${err.message}`);
              lastError = err;
              // Add a small delay between retries
              if (i < maxRetries - 1) {
                await new Promise(resolve => setTimeout(resolve, 1500));
              }
            }
          }
          
          throw new Error(`Failed after ${maxRetries} attempts: ${lastError.message}`);
        };
        
        // Display loading state
        this.loading = true;
        
        // Fetch both weather and marine data in parallel for better performance
        let weatherRes, marineRes;
        
        try {
          [weatherRes, marineRes] = await Promise.all([
            fetchWithRetry(weatherUrl),
            fetchWithRetry(marineUrl)
          ]);
        } catch (err) {
          console.error('API request failed after retries:', err);
          throw new Error(`Network issue: ${err.message}. The server might be busy, please try again later.`);
        }
        
        let weatherData, marineData;
        
        try {
          weatherData = await weatherRes.json();
          console.log('Weather data received successfully');
        } catch (err) {
          console.error('Failed to parse weather data:', err);
          throw new Error('Weather data format error. Please try again later.');
        }
        
        try {
          marineData = await marineRes.json();
          console.log('Marine data received successfully:', marineData);
          
          // Log specific marine data values for debugging
          console.log(`Wave height: ${marineData.wave_height} m`);
          console.log(`Swell height: ${marineData.swell_wave_height} m`);
          console.log(`Ocean current velocity: ${marineData.ocean_current_velocity} m/s`);
        } catch (err) {
          console.error('Failed to parse marine data:', err);
          throw new Error('Marine data format error. Please try again later.');
        }
        
        // Validate required data fields
        if (!weatherData.current || weatherData.current.temperature_2m === undefined) {
          console.error('Invalid weather data structure:', weatherData);
          throw new Error('Weather data is missing required fields');
        }
        
        if (marineData.wave_height === undefined) {
          console.error('Invalid marine data structure:', marineData);
          throw new Error('Marine data is missing required fields');
        }
        
        // Ensure current velocity is not undefined or null
        if (marineData.ocean_current_velocity === undefined || marineData.ocean_current_velocity === null) {
          console.warn('Ocean current velocity is missing, defaulting to 0');
          marineData.ocean_current_velocity = 0;
        }
        
        console.log('Beach data successfully fetched and validated');
        return {
          weather: weatherData,
          marine: marineData
        };
      } catch (err) {
        console.error('Beach data fetch error:', err);
        this.error = err.message;
        throw err;
      } finally {
        this.loading = false;
      }
    },
    async fetchSuggestions() {
      if (this.address.length < 2) {
        this.suggestions = [];
        this.suggestionPopupStyle.display = 'none';
        return;
      }
      
      try {
        // Add "beach" to the search query if it doesn't already contain it
        let searchQuery = this.address;
        if (!searchQuery.toLowerCase().includes('beach')) {
          searchQuery += ' beach';
        }
        
        const base = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(searchQuery)}&limit=15&countrycodes=au`;
        const res = await fetch(base, { headers: { 'User-Agent': 'BeachApp/1.0' } });
        
        if (!res.ok) {
          throw new Error(`Search failed with status: ${res.status}`);
        }
        
        const results = await res.json();
        
        // Log raw results for debugging
        console.log(`Found ${results.length} raw results for "${searchQuery}"`);
        
        // Filter using our new isActualBeach method
        this.suggestions = results.filter(item => this.isActualBeach(item));
        
        console.log(`Filtered to ${this.suggestions.length} actual beaches`);
        
        // Check if we found any valid beach results
        if (this.suggestions.length === 0) {
          console.log('No beach results found for:', searchQuery);
          // Try to log for debugging specific problematic inputs
          if (searchQuery.toLowerCase().includes('beach')) {
            console.log('Location may be a town/city named Beach, not an actual beach');
          }
          
          // Show a helpful error message to the user
          this.error = "No beaches found. Try using the beach name followed by state (e.g., 'Bondi Beach NSW')";
        } else {
          // Clear error message if we found results
          this.error = null;
        }
      
        // Position the popup if we have results
        this.positionSearchSuggestionsPopup();
      } catch (e) {
        console.error('Search error:', e);
        this.error = `Failed to search: ${e.message}`;
        this.suggestions = [];
        this.suggestionPopupStyle.display = 'none';
      }
    },
    
    positionSearchSuggestionsPopup() {
      // Only proceed if we have suggestions and the search input ref exists
      if (this.suggestions.length === 0 || !this.$refs.searchInput) {
        this.suggestionPopupStyle.display = 'none';
        return;
      }
      
      // Get the position of the search input
      const searchInput = this.$refs.searchInput;
      const rect = searchInput.getBoundingClientRect();
      
      // Get window dimensions for positioning context
      const windowWidth = window.innerWidth;
      const windowHeight = window.innerHeight;
      
      // Calculate popup width based on the input width
      const popupWidth = Math.min(rect.width, windowWidth - 40);
      
      // Calculate popup position
      let popupLeft = Math.max(20, rect.left);
      let popupTop = rect.bottom + 5;
      
      // Check if popup would extend beyond bottom of viewport
      const estimatedPopupHeight = Math.min(350, this.suggestions.length * 60);
      if (popupTop + estimatedPopupHeight > windowHeight) {
        // Position above the input if it would go off-screen below
        popupTop = Math.max(10, rect.top - estimatedPopupHeight - 10);
      }
      
      // Set the position and dimensions of the popup
      this.suggestionPopupStyle = {
        top: `${popupTop}px`,
        left: `${popupLeft}px`,
        width: `${popupWidth}px`,
        display: 'block',
        maxWidth: `${windowWidth - 40}px`,
        maxHeight: `${windowHeight * 0.7}px`, // Limit height to 70% of viewport
        zIndex: '9999' // Ensure popup appears above the spacing div
      };
      
      // Force browser reflow to ensure animations work properly
      if (document.querySelector('.suggestion-spacing')) {
        document.querySelector('.suggestion-spacing').getBoundingClientRect();
      }
    },
    async fetchCompareSuggestions(index) {
      const query = index === 1 ? this.compareAddress1 : this.compareAddress2;
      
      if (query.length < 2) {
        if (index === 1) {
          this.suggestions1 = [];
        } else {
          this.suggestions2 = [];
        }
        return;
      }
      
      try {
        // Add "beach" to the search query if it doesn't already contain it
        let searchQuery = query;
        if (!searchQuery.toLowerCase().includes('beach')) {
          searchQuery += ' beach';
        }
        
        // Home beach (index 1) can be any beach in the world
        // New beach (index 2) must be an Australian beach
        let base;
        if (index === 1) {
          // For home beach, search worldwide
          base = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(searchQuery)}&limit=15`;
        } else {
          // For new beach, limit to Australia
          base = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(searchQuery)}&limit=15&countrycodes=au`;
        }
        
        const res = await fetch(base, { headers: { 'User-Agent': 'BeachApp/1.0' } });
        
        if (!res.ok) {
          throw new Error(`Search failed with status: ${res.status}`);
        }
        
        const results = await res.json();
        
        // Log raw results
        console.log(`Found ${results.length} raw results for compare "${searchQuery}"`);
        
        // Apply filtering with our new method
        const filteredResults = results.filter(item => this.isActualBeach(item));
        
        console.log(`Filtered to ${filteredResults.length} actual beaches`);
        
        // Check if we found any valid beach results
        if (filteredResults.length === 0) {
          console.log('No beach results found for:', searchQuery);
          // Try to log for debugging specific problematic inputs
          if (searchQuery.toLowerCase().includes('beach')) {
            console.log('Location may be a town/city named Beach, not an actual beach');
          }
          
          // Show a helpful error message to the user
          const beachType = index === 1 ? "home" : "comparison";
          this.error = `No ${beachType} beaches found. Try using beach name followed by location (e.g., 'Bondi Beach NSW')`;
        } else {
          // Clear error message if we found results
          this.error = null;
        }
      
        if (index === 1) {
          this.suggestions1 = filteredResults;
        } else {
          this.suggestions2 = filteredResults;
        }
      } catch (e) {
        console.error('Search error:', e);
        this.error = `Failed to search: ${e.message}`;
        
        if (index === 1) {
          this.suggestions1 = [];
        } else {
          this.suggestions2 = [];
        }
      }
    },
    selectSuggestion(item) {
      this.address = item.display_name.split(',')[0];
      this.suggestions = [];
      this.suggestionPopupStyle.display = 'none';
      this.showBeachReport = false; // Reset beach report popup visibility
      
      const lat = parseFloat(item.lat);
      const lon = parseFloat(item.lon);
      
      this.loading = true;
      this.error = null;
      
      this.fetchBeachData(lat, lon)
        .then(data => {
          this.weather = data.weather;
          this.marine = data.marine;
          
          // Add debug logging for search beach feature
          console.log('===== SEARCH BEACH DATA =====');
          console.log(`Beach name: ${this.address}`);
          console.log(`Wave height: ${this.marine.wave_height} m`);
          console.log(`Current speed: ${this.marine.ocean_current_velocity} m/s`);
          
          // Calculate and log the beach condition category
          const beachData = [
            0, // Temperature - not used for categorization
            0, // Wind speed - not used for categorization anymore
            this.marine.wave_height || 0,
            this.marine.swell_wave_height || 0,
            this.marine.ocean_current_velocity || 0
          ];
          const category = this.getBeachConditionCategory(beachData);
          console.log(`Beach condition category: ${category}`);
          console.log(`Category thresholds: Wave height > 1.2m or Current > 0.5 m/s = HARSH`);
          console.log(`                      Wave height > 0.3m or Current > 0.3 m/s = MODERATE`);
          console.log(`                      Otherwise = CALM`);
          console.log('===========================');
          
          // Automatically show the beach report when data is loaded
          this.showBeachReport = true;
        })
        .catch(err => {
          this.error = err.message;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    selectCompareSuggestion(item, index) {
      if (index === 1) {
        this.compareAddress1 = item.display_name.split(',')[0];
        this.suggestions1 = [];
        this.selectedBeach1 = item;
      } else {
        this.compareAddress2 = item.display_name.split(',')[0];
        this.suggestions2 = [];
        this.selectedBeach2 = item;
      }
      
      this.error = null;
      
      console.log(`Selected beach ${index}: ${item.display_name} (${item.lat}, ${item.lon})`);
    },
    debouncedSearch() {
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.fetchSuggestions();
      }, 500);
    },
    debouncedSearchCompare1() {
      clearTimeout(this.searchCompareTimeout1);
      this.searchCompareTimeout1 = setTimeout(() => {
        this.fetchCompareSuggestions(1);
      }, 500);
    },
    debouncedSearchCompare2() {
      clearTimeout(this.searchCompareTimeout2);
      this.searchCompareTimeout2 = setTimeout(() => {
        this.fetchCompareSuggestions(2);
      }, 500);
    },
    
    // New helper function to detect if a location is an actual beach
    isActualBeach(item) {
      // If we have specific beach classification data, rely on that
      if ((item.class === 'natural' && item.type === 'beach') || 
          (item.category === 'natural' && item.type === 'beach')) {
        return true;
      }
        
      // Convert display name to lowercase for case-insensitive matching
      const displayName = item.display_name.toLowerCase();
      
      // REJECT conditions - return false immediately for these cases
      
      // 1. Reject if it starts with "Beach," as this is likely a town/place named "Beach"
      if (displayName.match(/^beach,/)) {
        console.log(`Rejected: Starts with "Beach,": ${displayName}`);
        return false;
      }
      
      // 2. Reject administrative entities like counties or states with "Beach" in the name
      if (item.type === 'administrative' || 
          item.type === 'city' || 
          item.type === 'town' || 
          item.type === 'county' || 
          item.type === 'suburb') {
        console.log(`Rejected: Administrative area with Beach in name: ${displayName}`);
        return false;
      }
      
      // 3. Reject streets, roads, etc.
      if (displayName.includes(' street') || 
          displayName.includes(' road') || 
          displayName.includes(' avenue') || 
          displayName.includes(' building')) {
        console.log(`Rejected: Street/road with Beach in name: ${displayName}`);
        return false;
      }
      
      // ACCEPT conditions - these strongly indicate a real beach
      
      // Check beach patterns that indicate it's an actual beach
      const hasBeachInName = displayName.includes('beach');
      
      // If it's a proper beach, these patterns are common:
      // "Something Beach" - "Bondi Beach", "Manly Beach", etc.
      if (displayName.match(/\w+\s+beach/) && !displayName.match(/^beach\s+\w+/)) {
        console.log(`Accepted: Has pattern like "Name Beach": ${displayName}`);
        return true;
      }
      
      // Look for coastal terms which help identify real beaches
      const hasCoastalTerms = 
        displayName.includes('coast') || 
        displayName.includes('bay') || 
        displayName.includes('ocean') || 
        displayName.includes('sea') || 
        displayName.includes('shore') ||
        displayName.includes('cove') ||
        displayName.includes('point') ||
        displayName.includes('sand') ||
        displayName.includes('water');
      
      // Accept if it has beach in name and coastal context
      if (hasBeachInName && hasCoastalTerms) {
        console.log(`Accepted: Has beach in name + coastal terms: ${displayName}`);
        return true;
      }
      
      // Reject by default for safety
      console.log(`Rejected by default: ${displayName}`);
      return false;
    },
    // Family Safety Assessment Methods
    getRipCurrentRisk(currentSpeed) {
      if (currentSpeed > 0.5) return 'High';
      if (currentSpeed > 0.3) return 'Moderate';
      return 'Low';
    },
    getRipCurrentRiskClass(currentSpeed) {
      if (currentSpeed > 0.5) return 'risk-high';
      if (currentSpeed > 0.3) return 'risk-moderate';
      return 'risk-low';
    },
    getRipCurrentExplanation(currentSpeed) {
      if (currentSpeed > 0.5) {
        return `High chance of rip currents. The strong current (${currentSpeed.toFixed(2)} m/s) creates powerful rips that can pull even adults 50-100 meters offshore in minutes. Children will be pulled out instantly, with little chance to react.`;
      } else if (currentSpeed > 0.3) {
        return `Moderate chance of rip currents forming. These currents (${currentSpeed.toFixed(2)} m/s) can pull children 20-30 meters offshore quickly. Adults may struggle to swim against these rips.`;
      } else {
        return `Lower chance of rip currents forming, but they can still develop. Current speed (${currentSpeed.toFixed(2)} m/s) means if caught in a rip, you'd be pulled about 5-10 meters offshore. Always watch for darker patches of water and less breaking waves.`;
      }
    },
    getWaveDanger(waveHeight, swellHeight) {
      const effectiveHeight = Math.max(waveHeight || 0, swellHeight || 0);
      if (effectiveHeight > 1.2) return 'High';
      if (effectiveHeight > 0.7) return 'Moderate';
      return 'Low';
    },
    getWaveDangerClass(waveHeight, swellHeight) {
      const effectiveHeight = Math.max(waveHeight || 0, swellHeight || 0);
      if (effectiveHeight > 1.2) return 'risk-high';
      if (effectiveHeight > 0.7) return 'risk-moderate';
      return 'risk-low';
    },
    getWaveExplanation(waveHeight, swellHeight) {
      const effectiveHeight = Math.max(waveHeight || 0, swellHeight || 0);
      if (effectiveHeight > 1.2) {
        return `Strong waves (${effectiveHeight.toFixed(2)} m) can knock down adults and children. Not safe for play or swimming today, especially for children.`;
      } else if (effectiveHeight > 0.7) {
        return `These waves (${effectiveHeight.toFixed(2)} m) can be challenging for children and inexperienced swimmers. Keep children in shallow water only.`;
      } else {
        return `Gentler waves (${effectiveHeight.toFixed(2)} m) are better for swimming, but always supervise children closely.`;
      }
    },
    getWaterFatigue(waterTemp) {
      if (waterTemp < 18) return 'High';
      if (waterTemp < 22) return 'Moderate';
      return 'Low';
    },
    getWaterFatigueClass(waterTemp) {
      if (waterTemp < 18) return 'risk-high';
      if (waterTemp < 22) return 'risk-moderate';
      return 'risk-low';
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
    getVisibilityControl(windSpeed) {
      if (windSpeed > 25) return 'High Risk';
      if (windSpeed > 15) return 'Moderate Risk';
      return 'Better Conditions';
    },
    getVisibilityControlClass(windSpeed) {
      if (windSpeed > 25) return 'risk-high';
      if (windSpeed > 15) return 'risk-moderate';
      return 'risk-low';
    },
    getVisibilityExplanation(windSpeed) {
      if (windSpeed > 25) {
        return `Very windy conditions (${windSpeed.toFixed(1)} km/h) create choppy water. Hard to see or hear your child if they struggle. Stay extremely close to children or consider a different activity today.`;
      } else if (windSpeed > 15) {
        return `Moderately windy (${windSpeed.toFixed(1)} km/h) conditions affect visibility and ability to hear calls for help. Keep children within arm's reach at all times.`;
      } else {
        return `Calmer conditions (${windSpeed.toFixed(1)} km/h) make it easier to monitor children, but always maintain close supervision.`;
      }
    },
    // Beach condition categorization methods
    getBeachConditionCategory(data) {
  const currentSpeed = data[4] || 0;
  const waveHeight = data[2] || 0;
  const swellHeight = data[3] || 0;
  
  // Calculate effective wave height
  const effectiveHeight = Math.max(waveHeight, swellHeight);
  
  // Add validation logging
  const category = this.calculateBeachCategory(currentSpeed, effectiveHeight);
  
  // Log when a beach is classified as HARSH
  if (category === "HARSH") {
    console.log('HARSH Beach detected:');
    console.log(`- Current Speed: ${currentSpeed} m/s (threshold > 0.5)`);
    console.log(`- Wave Height: ${waveHeight} m`);
    console.log(`- Swell Height: ${swellHeight} m`);
    console.log(`- Effective Height: ${effectiveHeight} m (threshold > 1.2)`);
    
    // Determine the trigger factor
    if (currentSpeed > 0.5) {
      console.log('- Triggered by: Strong current');
    } else if (effectiveHeight > 1.2) {
      console.log('- Triggered by: Large waves');
    }
  }
  
  return category;
},

// Helper method to calculate beach category
calculateBeachCategory(currentSpeed, effectiveHeight) {
  // Major risk factors - using explicit threshold checks for clarity
  if (currentSpeed > 0.5 || effectiveHeight > 1.2) {
    return "HARSH";
  } 
  // Moderate risk factors
  else if (currentSpeed > 0.3 || effectiveHeight > 0.7) {
    return "MODERATE";
  } 
  // Low risk factors
  else {
    return "CALM";
  }
},
    
    getBeachCategoryClass(data) {
      const category = this.getBeachConditionCategory(data);
      if (category === "HARSH") return "category-harsh";
      if (category === "MODERATE") return "category-moderate";
      return "category-calm";
    },
    
    getBeachConditionExplanation(data) {
      const category = this.getBeachConditionCategory(data);
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const swellHeight = data[3] || 0;
      const windSpeed = data[1] || 0;
      
      // Determine most dangerous factor
      const effectiveWaveHeight = Math.max(waveHeight, swellHeight);
      let primaryDanger = '';
      let dangerDetail = '';
      
      if (currentSpeed > waveHeight && currentSpeed > 0.3) {
        primaryDanger = 'strong currents';
        if (currentSpeed > 0.8) {
          dangerDetail = `Current speed (${currentSpeed.toFixed(1)} m/s) ${Math.round(currentSpeed/0.8) > 1 ? 'is ' + Math.round(currentSpeed/0.8) + '× faster than' : 'exceeds what'} Olympic swimmers can handle`;
        } else if (currentSpeed > 0.5) {
          dangerDetail = `Powerful rip currents pull swimmers ${Math.round(currentSpeed * 10)}m offshore in just 10 seconds`;
        } else {
          dangerDetail = `Moderate currents can quickly pull children beyond safe depth`;
        }
      } else if (effectiveWaveHeight > 0.5) {
        primaryDanger = 'high waves';
        if (effectiveWaveHeight > 1.5) {
          dangerDetail = `Waves (${effectiveWaveHeight.toFixed(1)}m) about ${Math.round(effectiveWaveHeight/1.2) > 1 ? Math.round(effectiveWaveHeight/1.2) + '× taller than' : 'the same height as'} a 10-year-old child`;
        } else if (effectiveWaveHeight > 1.0) {
          dangerDetail = `Strong waves (${effectiveWaveHeight.toFixed(1)}m) can knock down adults - similar to a dining table`;
        } else {
          dangerDetail = `Waves (${effectiveWaveHeight.toFixed(1)}m) may knock over children - about knee-height for adults`;
        }
      } else if (windSpeed > 20) {
        primaryDanger = 'strong winds';
        dangerDetail = `Wind (${Math.round(windSpeed)}km/h) creates poor visibility and difficult rescue conditions`;
      }
      
      // Create personalized description based on category
      if (category === "HARSH") {
        return `Dangerous conditions with ${primaryDanger}. ${dangerDetail}. Not safe for recreational swimming.`;
      } else if (category === "MODERATE") {
        return `Exercise caution due to ${primaryDanger}. ${dangerDetail}. Adults stay close to shore, supervise children.`;
      } else {
        if (effectiveWaveHeight < 0.3 && currentSpeed < 0.2) {
          return `Gentle conditions with small waves (${effectiveWaveHeight.toFixed(1)}m) and minimal current. Good for families.`;
        } else {
          return `Relatively calm conditions with manageable waves and currents. Supervise children.`;
        }
      }
    },
    // New methods for beach comparison recommendation
    getBeachSummary(data) {
      const category = this.getBeachConditionCategory(data);
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const swellHeight = data[3] || 0;
      const windSpeed = data[1] || 0;
      
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      let summary = '';
      
      // Main summary based on overall category
      if (category === "HARSH") {
        summary = `<p class="summary-intro">This beach has challenging conditions that pose significant risks.</p>`;
      } else if (category === "MODERATE") {
        summary = `<p class="summary-intro">This beach has moderate conditions that require caution.</p>`;
      } else {
        summary = `<p class="summary-intro">This beach has relatively calm and gentle conditions, generally suitable for families.</p>`;
      }
      
      // Add specific details about key dangers
      let keyDangers = [];
      
      // Wave height specific dangers
      if (effectiveHeight > 1.5) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌊</div>
            <div class="danger-content">
              <h4 class="danger-title">Dangerous waves (${effectiveHeight.toFixed(1)}m)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">Like being hit by a car - instantly knocked over, disoriented underwater</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">Can knock down and submerge even strong swimmers</span>
                </div>
              </div>
            </div>
          </div>
        `);
      } else if (effectiveHeight > 0.8) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌊</div>
            <div class="danger-content">
              <h4 class="danger-title">Challenging waves (${effectiveHeight.toFixed(1)}m)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">Will be knocked off feet and tumbled underwater, causing disorientation</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">Can push off balance and make standing difficult in deeper water</span>
                </div>
              </div>
            </div>
          </div>
        `);
      } else if (effectiveHeight > 0.4) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌊</div>
            <div class="danger-content">
              <h4 class="danger-title">Moderate waves (${effectiveHeight.toFixed(1)}m)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">Can knock over small children or push them underwater momentarily</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">Generally manageable but stay alert when waves break</span>
                </div>
              </div>
            </div>
          </div>
        `);
      }
      
      // Current specific dangers
      if (currentSpeed > 1.0) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌀</div>
            <div class="danger-content">
              <h4 class="danger-title">Extreme rip currents (${currentSpeed.toFixed(1)}m/s)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">Will be swept offshore in seconds with no ability to return</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">About ${Math.round(currentSpeed/0.3)}× faster than a 10-year-old child can swim - will rapidly exhaust even strong swimmers</span>
                </div>
              </div>
            </div>
          </div>
        `);
      } else if (currentSpeed > 0.5) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌀</div>
            <div class="danger-content">
              <h4 class="danger-title">Strong rip currents (${currentSpeed.toFixed(1)}m/s)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">No chance of swimming against this flow - will be carried beyond depth</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">Too strong to swim against for more than a minute before exhaustion</span>
                </div>
              </div>
            </div>
          </div>
        `);
      } else if (currentSpeed > 0.3) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">🌀</div>
            <div class="danger-content">
              <h4 class="danger-title">Moderate rip currents (${currentSpeed.toFixed(1)}m/s)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">👶 For children:</span>
                  <span class="impact-text">Will be pulled quickly into deeper water without ability to swim back</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">👤 For adults:</span>
                  <span class="impact-text">Even fit swimmers will struggle against this current</span>
                </div>
              </div>
            </div>
          </div>
        `);
      }
      
      // Visibility/wind specific dangers
      if (windSpeed > 25) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">💨</div>
            <div class="danger-content">
              <h4 class="danger-title">High winds (${windSpeed.toFixed(1)}km/h)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">Visibility:</span>
                  <span class="impact-text">Choppy water hides struggling swimmers, calls for help hard to hear</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">Safety:</span>
                  <span class="impact-text">Inflatable toys or paddleboards will blow offshore rapidly</span>
                </div>
              </div>
            </div>
          </div>
        `);
      } else if (windSpeed > 15) {
        keyDangers.push(`
          <div class="danger-card">
            <div class="danger-icon">💨</div>
            <div class="danger-content">
              <h4 class="danger-title">Moderate winds (${windSpeed.toFixed(1)}km/h)</h4>
              <div class="danger-impacts">
                <div class="impact-group">
                  <span class="impact-label">Visibility:</span>
                  <span class="impact-text">Harder to spot swimmers in trouble, calls for help may not be heard</span>
                </div>
                <div class="impact-group">
                  <span class="impact-label">Safety:</span>
                  <span class="impact-text">Keep children within close visual range at all times</span>
                </div>
              </div>
            </div>
          </div>
        `);
      }
      
      // Add key dangers to summary if there are any
      if (keyDangers.length > 0) {
        summary += '<div class="key-dangers">' + keyDangers.join('') + '</div>';
      }
      
      return summary;
    },
    
    getBestForGroups(data) {
      const category = this.getBeachConditionCategory(data);
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const swellHeight = data[3] || 0;
      const windSpeed = data[1] || 0;
      
      const effectiveHeight = Math.max(waveHeight, swellHeight);
      
      // Determine the most restrictive factor
      let highestDanger = 0; // 0=low, 1=moderate, 2=high
      
      if (currentSpeed > 0.5 || effectiveHeight > 1.2 || windSpeed > 25) {
        highestDanger = 2; // High danger
      } else if (currentSpeed > 0.3 || effectiveHeight > 0.7 || windSpeed > 15) {
        highestDanger = 1; // Moderate danger
      }
      
      if (highestDanger === 2) {
        if (currentSpeed > 1.0 || effectiveHeight > 1.8) {
          return "Only experienced adult swimmers familiar with ocean conditions";
        } else {
          return "Strong adult swimmers only - not suitable for children";
        }
      } else if (highestDanger === 1) {
        if (currentSpeed > 0.4 || effectiveHeight > 1.0) {
          return "Adults and teenagers with swimming experience";
        } else {
          return "Families with older children (8+) under close supervision";
        }
      } else {
        return "All family members including young children (with supervision)";
      }
    },
    
    getBeachAdvice(data) {
      const category = this.getBeachConditionCategory(data);
      const currentSpeed = data[4] || 0;
      const waveHeight = data[2] || 0;
      const windSpeed = data[1] || 0;
      
      let advice = [];
      
      if (category === "HARSH") {
        advice.push("Keep inexperienced swimmers out of the water");
        advice.push("Adults should not swim alone");
        if (currentSpeed > 0.5) {
          advice.push("Watch for rip currents - darker patches with fewer breaking waves");
        }
      } else if (category === "MODERATE") {
        advice.push("Keep children in shallow water only");
        advice.push("Maintain constant supervision of non-swimmers");
        if (windSpeed > 15) {
          advice.push("Wind may make it difficult to hear calls for help");
        }
      } else {
        // No default advice for calm conditions
        if (waveHeight > 0.3) {
          advice.push("Even small waves can unbalance young children");
        }
      }
      
      return advice;
    },
    
    getComparisonConclusion() {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return "";
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      const homeName = this.compareChartData.datasets[0].label;
      const newName = this.compareChartData.datasets[1].label;
      
      // Check for key danger factors
      const homeCurrentSpeed = homeData[4] || 0;
      const newCurrentSpeed = newData[4] || 0;
      const homeWaveHeight = Math.max(homeData[2] || 0, homeData[3] || 0);
      const newWaveHeight = Math.max(newData[2] || 0, newData[3] || 0);
      
      // Calculate overall safety difference
      const homeSafetyScore = this.calculateSafetyScore(homeData);
      const newSafetyScore = this.calculateSafetyScore(newData);
      const scoreDifference = newSafetyScore - homeSafetyScore;
      
      let conclusionText = "";
      
      // Wave height comparison
      let waveComparison = "";
      if (Math.abs(homeWaveHeight - newWaveHeight) > 0.2) {
        if (newWaveHeight > homeWaveHeight) {
          // Check if home wave height is near zero
          if (homeWaveHeight < 0.1) {
            waveComparison = `Waves at ${newName} are much taller than your home beach, similar to ${newWaveHeight > 1.5 ? 'a bus' : (newWaveHeight > 1 ? 'a car' : (newWaveHeight > 0.8 ? 'a 10-year-old child' : 'a 6-year-old child'))}.`;
          } else {
            const ratio = Math.round(newWaveHeight/homeWaveHeight);
            let heightCompText = 'about the same height';
            if (ratio > 1) {
              heightCompText = ratio + '× taller';
            }
            waveComparison = `Waves at ${newName} are ${heightCompText} as your home beach, similar to ${newWaveHeight > 1.5 ? 'a bus' : (newWaveHeight > 1 ? 'a car' : (newWaveHeight > 0.8 ? 'a 10-year-old child' : 'a 6-year-old child'))}.`;
          }
        } else {
          waveComparison = `Waves at ${newName} are smaller than your home beach, making swimming easier.`;
        }
      } else {
        waveComparison = `Wave heights at both beaches are similar.`;
      }
      
      // Current comparison
      let currentComparison = "";
      if (Math.abs(homeCurrentSpeed - newCurrentSpeed) > 0.1) {
        if (newCurrentSpeed > homeCurrentSpeed) {
          // Check if home current speed is near zero
          if (homeCurrentSpeed < 0.1) {
            currentComparison = `Currents at ${newName} are much stronger than your home beach ${newCurrentSpeed > 0.8 ? '- about ' + Math.round(newCurrentSpeed/0.3) + '× faster than a 10-year-old child can swim' : '- comparable to a casual cyclist'}.`;
          } else {
            const ratio = Math.round(newCurrentSpeed/homeCurrentSpeed);
            let speedCompText = 'about the same speed';
            if (ratio > 1) {
              speedCompText = ratio + '× faster';
            }
            let childSwimText = '- comparable to a casual cyclist';
            if (newCurrentSpeed > 0.8) {
              const childSwimRatio = Math.round(newCurrentSpeed/0.3);
              if (childSwimRatio > 1) {
                childSwimText = '- about ' + childSwimRatio + '× faster than a 10-year-old child can swim';
              } else {
                childSwimText = '- about the same speed as a 10-year-old child can swim';
              }
            }
            currentComparison = `Currents at ${newName} are ${speedCompText} as your home beach ${childSwimText}.`;
          }
        } else {
          currentComparison = `Currents at ${newName} are gentler than your home beach, reducing the risk of being pulled offshore.`;
        }
      } else {
        currentComparison = `Current speeds at both beaches are similar.`;
      }
      
      // Significant difference - new beach is more dangerous
      if (scoreDifference > 1.5) {
        conclusionText = `<strong>${newName} has much more challenging conditions than home.</strong> `;
        
        // Add specific comparisons
        if (newWaveHeight > homeWaveHeight && newWaveHeight > 0.8) {
          conclusionText += waveComparison + " ";
        }
        
        if (newCurrentSpeed > homeCurrentSpeed && newCurrentSpeed > 0.3) {
          conclusionText += currentComparison + " ";
        }
        
        conclusionText += `<strong>Use extra caution or choose a patrolled area.</strong>`;
      }
      // Moderate difference - new beach is more dangerous
      else if (scoreDifference > 0.5) {
        conclusionText = `<strong>${newName} is somewhat more challenging than home.</strong> `;
        
        // Add specific comparisons
        if (Math.abs(homeWaveHeight - newWaveHeight) > 0.2 || Math.abs(homeCurrentSpeed - newCurrentSpeed) > 0.1) {
          if (newWaveHeight > homeWaveHeight) {
            conclusionText += waveComparison + " ";
          }
          
          if (newCurrentSpeed > homeCurrentSpeed) {
            conclusionText += currentComparison + " ";
          }
        }
        
        conclusionText += `<strong>Swim between flags and supervise children closely.</strong>`;
      }
      // New beach is similar or safer 
      else if (scoreDifference >= -0.5) {
        conclusionText = `<strong>${newName} has similar conditions to your home beach.</strong> `;
        
        // Add comparison if there are still differences
        if (Math.abs(homeWaveHeight - newWaveHeight) > 0.2 || Math.abs(homeCurrentSpeed - newCurrentSpeed) > 0.1) {
          if (Math.abs(homeWaveHeight - newWaveHeight) > 0.2) {
            conclusionText += waveComparison + " ";
          }
          
          if (Math.abs(homeCurrentSpeed - newCurrentSpeed) > 0.1) {
            conclusionText += currentComparison + " ";
          }
        }
        
        conclusionText += `<strong>Swim between flags and stay alert.</strong>`;
      }
      // New beach is significantly safer
      else {
        conclusionText = `<strong>${newName} has gentler conditions than your home beach - you're well prepared!</strong>`;
      }
      
      return conclusionText;
    },
    
    calculateSafetyScore(data) {
      const currentSpeed = data[4] || 0;
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      
      // Calculate current score with non-linear scaling for more accuracy
      let currentScore = 0;
      if (currentSpeed > 0.8) currentScore = currentSpeed * 4; // Dangerous currents weighted heavily
      else if (currentSpeed > 0.5) currentScore = currentSpeed * 3; // Strong currents
      else if (currentSpeed > 0.3) currentScore = currentSpeed * 2; // Moderate currents
      else currentScore = currentSpeed; // Mild currents
      
      // Calculate wave score with non-linear scaling
      let waveScore = 0;
      if (waveHeight > 1.2) waveScore = waveHeight * 3; // Dangerous waves weighted heavily
      else if (waveHeight > 0.7) waveScore = waveHeight * 2; // Moderate waves
      else waveScore = waveHeight; // Calm waves
      
      // Log individual scores for debugging
      console.log(`Wave Height: ${waveHeight}m → Score: ${waveScore.toFixed(2)}`);
      console.log(`Current Speed: ${currentSpeed}m/s → Score: ${currentScore.toFixed(2)}`);
      
      return currentScore + waveScore;
    },
    
    calculateSafetyDifference() {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return 0;
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      const homeName = this.compareChartData.datasets[0].label;
      const newName = this.compareChartData.datasets[1].label;
      
      const homeSafetyScore = this.calculateSafetyScore(homeData);
      const newSafetyScore = this.calculateSafetyScore(newData);
      const diff = newSafetyScore - homeSafetyScore;
      
      // Add detailed logging to understand the calculation
      console.log('===== BEACH SAFETY CALCULATION =====');
      console.log(`Home Beach (${homeName}): Safety Score = ${homeSafetyScore.toFixed(2)}`);
      console.log(`New Beach (${newName}): Safety Score = ${newSafetyScore.toFixed(2)}`);
      console.log(`Safety Difference: ${diff.toFixed(2)}`);
      console.log(`Readiness Answer: ${diff > 2 ? 'Not Likely' : 
                  (diff > 1 ? 'Somewhat Prepared' : 
                  (diff > 0.3 ? 'Mostly Prepared' : 
                  (diff >= -0.5 ? 'Yes, Prepared' : 'Very Well Prepared')))}`);
      console.log('==================================');
      
      return diff;
    },
    
    getReadinessAnswer() {
      const diff = this.calculateSafetyDifference();
      
      if (diff > 2) {
        return "Not Likely";
      } else if (diff > 1) {
        return "Somewhat Prepared";
      } else if (diff > 0.3) {
        return "Mostly Prepared";
      } else if (diff >= -0.5) {
        return "Yes, Prepared";
      } else {
        // If home beach is significantly more dangerous than new beach
        return "Very Well Prepared";
      }
    },
    
    getConditionTerm(data, type) {
  if (type === 'wave') {
    const waveHeight = Math.max(data[2] || 0, data[3] || 0);
    if (waveHeight > 1.2) return "Dangerous";
    if (waveHeight > 0.3 && waveHeight <= 1.2) return "Moderate";
    return "Calm";
  } else if (type === 'current') {
    const currentSpeed = data[4] || 0;
    if (currentSpeed > 0.8) return "Dangerous";
    if (currentSpeed > 0.5 && currentSpeed <= 0.8) return "Strong";
    if (currentSpeed > 0.3 && currentSpeed <= 0.5) return "Moderate";
    return "Mild";
  }
  return "Unknown";
},
    
    getComparativeAdvantages(betterData, worseData) {
      return "";
    },
    // Add these methods to handle the suitability for different age groups based on beach data
    getChildSafety(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 0.8 || currentSpeed > 0.3) {
        return '❌';
      } else if (waveHeight > 0.5 || currentSpeed > 0.2) {
        return '⚠️';
      } else {
        return '✅';
      }
    },

    getChildSafetyClass(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 0.8 || currentSpeed > 0.3) {
        return 'safety-not-safe';
      } else if (waveHeight > 0.5 || currentSpeed > 0.2) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },

    getOlderChildSafety(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 1.2 || currentSpeed > 0.5) {
        return '❌';
      } else if (waveHeight > 0.7 || currentSpeed > 0.3) {
        return '⚠️';
      } else {
        return '✅';
      }
    },

    getOlderChildSafetyClass(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 1.2 || currentSpeed > 0.5) {
        return 'safety-not-safe';
      } else if (waveHeight > 0.7 || currentSpeed > 0.3) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },

    getAdultSafety(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 1.8 || currentSpeed > 0.8) {
        return '❌';
      } else if (waveHeight > 1.2 || currentSpeed > 0.5) {
        return '⚠️';
      } else {
        return '✅';
      }
    },

    getAdultSafetyClass(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      const currentSpeed = data[4] || 0;
      
      if (waveHeight > 1.8 || currentSpeed > 0.8) {
        return 'safety-not-safe';
      } else if (waveHeight > 1.2 || currentSpeed > 0.5) {
        return 'safety-caution';
      } else {
        return 'safety-safe';
      }
    },
    
    // New helper method to identify key differences between beaches
    getKeyDifferencesFactor(data1, data2) {
      return "";
    },
    getKeyDifferencesBetweenBeaches() {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return [];
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      const homeName = this.compareChartData.datasets[0].label;
      const newName = this.compareChartData.datasets[1].label;
      
      // If comparing the same beach (by name), return empty array
      if (homeName === newName) {
        return [];
      }
      
      const differences = [];
      
      // Compare rip currents
      const homeCurrentSpeed = homeData[4] || 0;
      const newCurrentSpeed = newData[4] || 0;
      const currentDiff = Math.abs(homeCurrentSpeed - newCurrentSpeed).toFixed(2);
      
      if (Math.abs(homeCurrentSpeed - newCurrentSpeed) > 0.1) {
        if (newCurrentSpeed > homeCurrentSpeed) {
          differences.push({
            type: 'currents',
            title: `Stronger Rip Currents at ${newName}`,
            description: `The rip currents at ${newName} (${newCurrentSpeed.toFixed(2)} m/s) are ${currentDiff} m/s stronger than at ${homeName} (${homeCurrentSpeed.toFixed(2)} m/s). If caught in a rip, you'd be pulled about ${Math.round(newCurrentSpeed * 10)} meters offshore in just 10 seconds - ${Math.round((newCurrentSpeed - homeCurrentSpeed) * 10)} meters further than at your home beach.`,
            impact: `This means you'll need to be much more vigilant about spotting rips (dark patches of water with fewer breaking waves) and keeping children closer to shore.`,
            severity: newCurrentSpeed > 0.5 ? 'high' : (newCurrentSpeed > 0.3 ? 'moderate' : 'low')
          });
        } else {
          differences.push({
            type: 'currents',
            title: `Stronger Rip Currents at ${homeName}`,
            description: `The rip currents at ${homeName} (${homeCurrentSpeed.toFixed(2)} m/s) are ${currentDiff} m/s stronger than at ${newName} (${newCurrentSpeed.toFixed(2)} m/s). Your experience at home has prepared you for stronger rips than what you'll find here.`,
            impact: `This is actually an advantage - the gentler currents at ${newName} mean less risk of being pulled offshore unexpectedly.`,
            severity: homeCurrentSpeed > 0.5 ? 'high' : (homeCurrentSpeed > 0.3 ? 'moderate' : 'low')
          });
        }
      }
      
      // Compare wave heights
      const homeWaveHeight = Math.max(homeData[2] || 0, homeData[3] || 0);
      const newWaveHeight = Math.max(newData[2] || 0, newData[3] || 0);
      const waveDiff = Math.abs(homeWaveHeight - newWaveHeight).toFixed(2);
      
      if (Math.abs(homeWaveHeight - newWaveHeight) > 0.2) {
        if (newWaveHeight > homeWaveHeight) {
          differences.push({
            type: 'waves',
            title: `Larger Waves at ${newName}`,
            description: `The waves at ${newName} (${newWaveHeight.toFixed(2)} m) are ${waveDiff} m taller than at ${homeName} (${homeWaveHeight.toFixed(2)} m). Waves this size can knock over an ${newWaveHeight > 1.5 ? 'adult' : 'child'} and create much stronger impact forces.`,
            impact: `These larger waves will feel about ${Math.round((newWaveHeight/homeWaveHeight - 1) * 100)}% more powerful than what you're used to, making it harder to maintain footing in the water.`,
            severity: newWaveHeight > 1.2 ? 'high' : (newWaveHeight > 0.7 ? 'moderate' : 'low')
          });
        } else {
          differences.push({
            type: 'waves',
            title: `Smaller Waves at ${newName}`,
            description: `The waves at ${newName} (${newWaveHeight.toFixed(2)} m) are ${waveDiff} m smaller than at ${homeName} (${homeWaveHeight.toFixed(2)} m).`,
            impact: `You'll find the gentler waves here easier to manage than what you're used to at home.`,
            severity: 'low'
          });
        }
      }
      
      // Compare wind speeds
      const homeWindSpeed = homeData[1] || 0;
      const newWindSpeed = newData[1] || 0;
      const windDiff = Math.abs(homeWindSpeed - newWindSpeed).toFixed(1);
      
      if (Math.abs(homeWindSpeed - newWindSpeed) > 5) {
        if (newWindSpeed > homeWindSpeed) {
          differences.push({
            type: 'wind',
            title: `Windier Conditions at ${newName}`,
            description: `${newName} is experiencing stronger winds (${newWindSpeed.toFixed(1)} km/h) than you're used to at ${homeName} (${homeWindSpeed.toFixed(1)} km/h).`,
            impact: `Stronger winds create choppier water, making it harder to see swimmers in trouble and hear calls for help. Wind also creates surface currents that can push inflatable toys offshore very quickly.`,
            severity: newWindSpeed > 25 ? 'high' : (newWindSpeed > 15 ? 'moderate' : 'low')
          });
        } else {
          differences.push({
            type: 'wind',
            title: `Calmer Conditions at ${newName}`,
            description: `${newName} has lighter winds (${newWindSpeed.toFixed(1)} km/h) compared to ${homeName} (${homeWindSpeed.toFixed(1)} km/h).`,
            impact: `The calmer wind conditions make for better visibility and easier communication, improving safety compared to your home beach.`,
            severity: 'low'
          });
        }
      }
      
      // Return the differences - don't add a "Similar Conditions" entry
      return differences;
    },

    // Complete replacement of the getBeachSimilarities method
    getBeachSimilarities() {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return [];
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      const homeName = this.compareChartData.datasets[0].label;
      const newName = this.compareChartData.datasets[1].label;
      
      // If comparing the same beach (by name), return empty array
      if (homeName === newName) {
        return [];
      }
      
      const similarities = [];
      
      // Compare rip currents
      const homeCurrentSpeed = homeData[4] || 0;
      const newCurrentSpeed = newData[4] || 0;
      
      if (Math.abs(homeCurrentSpeed - newCurrentSpeed) <= 0.1) {
        let severity = 'low';
        if (homeCurrentSpeed > 0.5) severity = 'high';
        else if (homeCurrentSpeed > 0.3) severity = 'moderate';
        
        similarities.push({
          type: 'currents',
          title: `Similar Rip Current Risk`,
          description: `Both ${homeName} (${homeCurrentSpeed.toFixed(2)} m/s) and ${newName} (${newCurrentSpeed.toFixed(2)} m/s) have comparable rip current strength.`,
          impact: homeCurrentSpeed > 0.3 
            ? `Both beaches require vigilance for rip currents. Your experience watching for rips at home will transfer well here.` 
            : `Both beaches have relatively mild currents, making them similarly safer from rip current risks.`,
          severity: severity
        });
      }
      
      // Compare wave heights
      const homeWaveHeight = Math.max(homeData[2] || 0, homeData[3] || 0);
      const newWaveHeight = Math.max(newData[2] || 0, newData[3] || 0);
      
      if (Math.abs(homeWaveHeight - newWaveHeight) <= 0.2) {
        let severity = 'low';
        if (homeWaveHeight > 1.2) severity = 'high';
        else if (homeWaveHeight > 0.7) severity = 'moderate';
        
        similarities.push({
          type: 'waves',
          title: `Similar Wave Conditions`,
          description: `Both beaches have waves of comparable height (${homeName}: ${homeWaveHeight.toFixed(2)} m, ${newName}: ${newWaveHeight.toFixed(2)} m).`,
          impact: homeWaveHeight > 0.7 
            ? `The wave force will feel familiar to you - your family already knows how to handle these kinds of waves.` 
            : `Both locations offer similarly gentle waves, providing a consistent swimming experience.`,
          severity: severity
        });
      }
      
      // Compare wind speeds
      const homeWindSpeed = homeData[1] || 0;
      const newWindSpeed = newData[1] || 0;
      
      if (Math.abs(homeWindSpeed - newWindSpeed) <= 5) {
        let severity = 'low';
        if (homeWindSpeed > 25) severity = 'high';
        else if (homeWindSpeed > 15) severity = 'moderate';
        
        similarities.push({
          type: 'wind',
          title: `Similar Wind Conditions`,
          description: `Both beaches have comparable wind speeds (${homeName}: ${homeWindSpeed.toFixed(1)} km/h, ${newName}: ${newWindSpeed.toFixed(1)} km/h).`,
          impact: homeWindSpeed > 15 
            ? `You're already accustomed to watching how wind affects water visibility and safety at your home beach.` 
            : `Both beaches offer similarly calm wind conditions, making it easier to spot swimmers in trouble.`,
          severity: severity
        });
      }
      
      // Compare overall temperature
      const homeTemp = homeData[0] || 0;
      const newTemp = newData[0] || 0;
      
      if (Math.abs(homeTemp - newTemp) <= 2) {
        similarities.push({
          type: 'weather',
          title: `Similar Air Temperature`,
          description: `The air temperature is comparable at both beaches (${homeName}: ${homeTemp.toFixed(1)}°C, ${newName}: ${newTemp.toFixed(1)}°C).`,
          impact: `Your family will experience similar comfort levels out of the water, with similar sunburn risk and need for hydration.`,
          severity: 'low'
        });
      }
      
      return similarities;
    },
    // Add method to check if beaches are the same
    areSameBeaches() {
      if (!this.selectedBeach1 || !this.selectedBeach2) {
        return false;
      }
      
      // Check if both beaches have same name and similar coordinates (within a small threshold)
      const nameMatch = this.selectedBeach1.display_name === this.selectedBeach2.display_name;
      
      // Check coordinates with a small threshold to account for minor variations
      const latThreshold = 0.01; // About 1km
      const lonThreshold = 0.01;
      
      const latDiff = Math.abs(parseFloat(this.selectedBeach1.lat) - parseFloat(this.selectedBeach2.lat));
      const lonDiff = Math.abs(parseFloat(this.selectedBeach1.lon) - parseFloat(this.selectedBeach2.lon));
      
      const coordsMatch = latDiff < latThreshold && lonDiff < lonThreshold;
      
      return nameMatch || coordsMatch; // Return true if either name or coordinates match
    },
    getWaveRiskPosition() {
      if (!this.marine || !this.marine.wave_height) return '16.7%';
      const h = this.marine.wave_height;
      
      // 0-0.3 m: safe (0-33%)
      // 0.3-1.2 m: caution (33-66%) 
      // >1.2 m: danger (66-100%)
      
      if (h > 1.2) {
        // Position within the danger segment (66-100%)
        if (h >= 1.8) return '90%';  // Far into danger zone
        if (h >= 1.5) return '80%';  // Deep in danger zone
        return '70%';  // Start of danger zone
      } 
      else if (h > 0.7) {
        // Position within the upper caution segment (50-66%)
        return '58%';  // Between middle and danger
      }
      else if (h > 0.3) {
        // Position within the lower caution segment (33-50%)
        return '42%';  // Between safe and middle
      }
      
      // Safe segment
      if (h > 0.2) return '25%';     // Upper safe zone
      return '16.7%';                // Lower safe zone
    },
    
    getCurrentRiskPosition() {
      if (!this.marine || !this.marine.ocean_current_velocity) return '16.7%';
      
      const currentSpeed = this.marine.ocean_current_velocity;
      
      // Calculate position on a scale
      // 0-0.3 m/s: safe (0-33%)
      // 0.3-0.8 m/s: caution (33-66%) 
      // >0.8 m/s: danger (66-100%)
      
      if (currentSpeed > 0.8) {
        // Position within the danger segment (66-100%)
        if (currentSpeed >= 1.2) return '90%';  // Far into danger zone
        if (currentSpeed >= 1.0) return '80%';  // Deep in danger zone
        return '70%';  // Start of danger zone
      } 
      else if (currentSpeed > 0.5) {
        // Position within the upper caution segment (50-66%)
        return '58%';  // Between middle and danger
      }
      else if (currentSpeed > 0.3) {
        // Position within the lower caution segment (33-50%)
        return '42%';  // Between safe and middle
      }
      
      // Safe segment
      if (currentSpeed > 0.2) return '25%';     // Upper safe zone
      return '16.7%';                           // Lower safe zone
    },
    
    getSafetyImpactSummary() {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return [];
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      const homeName = this.compareChartData.datasets[0].label;
      const newName = this.compareChartData.datasets[1].label;
      
      // Get the effective wave heights and current speeds
      const homeWaveHeight = Math.max(homeData[2] || 0, homeData[3] || 0);
      const newWaveHeight = Math.max(newData[2] || 0, newData[3] || 0);
      const homeCurrentSpeed = homeData[4] || 0;
      const newCurrentSpeed = newData[4] || 0;
      
      const impacts = [];
      
      // Wave height impacts
      if (newWaveHeight > homeWaveHeight + 0.2) {
        if (newWaveHeight > 1.2) {
          impacts.push({
            type: 'danger',
            icon: '🌊',
            text: `Waves at ${newName} can easily knock over adults, whereas ${homeName} has gentler waves. Keep children at the water's edge only.`
          });
        } else if (newWaveHeight > 0.8) {
          impacts.push({
            type: 'warning',
            icon: '🌊',
            text: `${newName} has waves that can knock children over but may only reach up to adults' hips. Stay within arm's reach of children.`
          });
        } else {
          impacts.push({
            type: 'info',
            icon: '🌊',
            text: `${newName} has slightly larger waves than ${homeName}, but both are relatively manageable with proper supervision.`
          });
        }
      } else if (homeWaveHeight > newWaveHeight + 0.2) {
        impacts.push({
          type: 'safe',
          icon: '🌊',
          text: `${newName} has gentler waves than you're used to at ${homeName}, making swimming conditions more favorable.`
        });
      }
      
      // Current impacts
      if (newCurrentSpeed > homeCurrentSpeed + 0.1) {
        if (newCurrentSpeed > 0.8) {
          impacts.push({
            type: 'danger',
            icon: '🌀',
            text: `${newName} has dangerously strong rip currents that can sweep swimmers 50+ meters offshore in seconds. These currents are about ${Math.round(newCurrentSpeed/0.3)}× faster than a 10-year-old child can swim.`
          });
        } else if (newCurrentSpeed > 0.5) {
          impacts.push({
            type: 'warning',
            icon: '🌀',
            text: `Rip currents at ${newName} are significantly stronger than at ${homeName}. Stay between the flags and maintain constant visual contact with children.`
          });
        } else if (newCurrentSpeed > 0.3) {
          impacts.push({
            type: 'info',
            icon: '🌀',
            text: `${newName} has stronger currents than ${homeName}, which can pull children beyond safe depth quickly. Keep children in shallow water only.`
          });
        }
      } else if (homeCurrentSpeed > newCurrentSpeed + 0.1) {
        impacts.push({
          type: 'safe',
          icon: '🌀',
          text: `${newName} has gentler currents than you're used to at ${homeName}, reducing the risk of being pulled offshore unexpectedly.`
        });
      }
      
      // Combined risk assessment
      if (newWaveHeight > 1.0 && newCurrentSpeed > 0.5) {
        impacts.push({
          type: 'danger',
          icon: '⚠️',
          text: `The combination of large waves and strong currents at ${newName} creates significant hazards. Consider a more sheltered beach for family swimming.`
        });
      }
      
      return impacts;
    },
    shouldShowVisualCard(type) {
      if (!this.compareChartData || !this.compareChartData.datasets || this.compareChartData.datasets.length < 2) {
        return false;
      }
      
      const homeData = this.compareChartData.datasets[0].data;
      const newData = this.compareChartData.datasets[1].data;
      
      if (type === 'wave') {
        return homeData[2] !== undefined && newData[2] !== undefined;
      } else if (type === 'current') {
        // Only show current cards if at least one beach has a current > 0
        return homeData[4] !== undefined && newData[4] !== undefined && 
               (homeData[4] > 0 || newData[4] > 0);
      }
      
      return false;
    },
    getWaveImpactText(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      if (waveHeight > 1.2) {
        const heightRatio = Math.round(waveHeight/1.2);
        let heightText = 'about the same height as';
        if (heightRatio > 1) {
          heightText = heightRatio + '× taller than';
        }
        return `These waves are ${heightText} a 10-year-old child and can easily knock them underwater`;
      } else if (waveHeight > 0.7) {
        return `These waves can reach up to a child's chest and have enough force to unbalance them`;
      } else {
        return `These smaller waves are generally below waist-height for a 6-year-old child`;
      }
    },
    getWaveAdviceText(data) {
      const waveHeight = Math.max(data[2] || 0, data[3] || 0);
      if (waveHeight > 1.2) {
        return `Adults should stay in shallow water and keep children at the water's edge only`;
      } else if (waveHeight > 0.7) {
        return `Keep children within arm's reach at all times`;
      } else {
        return `Still supervise children closely at all times`;
      }
    },
    getCurrentImpactText(data) {
      const currentSpeed = data[4] || 0;
      if (currentSpeed > 0.8) {
        const speedRatio = Math.round(currentSpeed/0.3);
        let speedText = 'about the same speed as';
        if (speedRatio > 1) {
          speedText = speedRatio + '× faster than';
        }
        return `This current is ${speedText} a 10-year-old child can swim. They'll be swept away within seconds`;
      } else if (currentSpeed > 0.5) {
        return `This current is about 2× faster than a 10-year-old child can swim against, making it difficult for them to make progress`;
      } else {
        return `This current is slower than most 10-year-old children can swim, making conditions more manageable`;
      }
    },
    getCurrentAdviceText(data) {
      const currentSpeed = data[4] || 0;
      if (currentSpeed > 0.8) {
        return `Even strong adult swimmers will struggle against these powerful currents`;
      } else if (currentSpeed > 0.5) {
        return `Keep children in shallow water and within arm's reach`;
      } else {
        return `Still supervise constantly and be aware of changing conditions`;
      }
    },
    // Add retrySearch method to handle retry functionality in the search tab
    retrySearch() {
      if (this.address) {
        this.error = null;
        this.loading = true;
        
        // Find the selected beach from suggestions if possible
        const selectedBeach = this.suggestions.find(item => 
          item.display_name.split(',')[0].trim() === this.address.trim()
        );
        
        if (selectedBeach) {
          const lat = parseFloat(selectedBeach.lat);
          const lon = parseFloat(selectedBeach.lon);
          
          this.fetchBeachData(lat, lon)
            .then(data => {
              this.weather = data.weather;
              this.marine = data.marine;
            })
            .catch(err => {
              this.error = err.message;
            })
            .finally(() => {
              this.loading = false;
            });
        } else {
          // If no valid beach is found, just reset loading state without showing error message
          this.loading = false;
        }
      } else {
        // Just reset loading state without error message
        this.loading = false;
      }
    },
    
    // Event handlers for popup positioning
    handleWindowResize() {
      // When window is resized, reposition the popup if it's visible
      if (this.activeTab === 'search' && this.suggestions.length > 0 && this.suggestionPopupStyle.display === 'block') {
        this.positionSearchSuggestionsPopup();
      }
    },
    
    handleOutsideClick(event) {
      // Handle search suggestions popup
      if (this.suggestionPopupStyle.display === 'block') {
        // Get references to the search input and popup
        const searchInput = this.$refs.searchInput;
        const popup = document.querySelector('.search-suggestions-popup');
        
        // If the click is outside both the search input and popup, close the popup
        if (searchInput && popup && 
            !searchInput.contains(event.target) && 
            !popup.contains(event.target)) {
          this.suggestions = []; // Clear suggestions to fully hide the popup
          this.suggestionPopupStyle.display = 'none';
        }
      }
      
      // Handle beach report popup - close when clicking on the overlay (not on the content)
      if (this.showBeachReport) {
        const reportPopup = document.querySelector('.beach-report-popup');
        const reportOverlay = document.querySelector('.beach-report-popup-overlay');
        
        // If we clicked directly on the overlay (not on the popup content), close it
        if (reportOverlay && reportPopup && 
            event.target === reportOverlay && 
            !reportPopup.contains(event.target)) {
          this.showBeachReport = false;
        }
      }
      
      // Handle beach comparison popup - close when clicking on the overlay (not on the content)
      if (this.showCompareReport) {
        const comparePopups = document.querySelectorAll('.beach-report-popup');
        const compareOverlays = document.querySelectorAll('.beach-report-popup-overlay');
        
        // Find the comparison popup (the last one if multiple exist)
        const comparePopup = comparePopups[comparePopups.length - 1];
        const compareOverlay = compareOverlays[compareOverlays.length - 1];
        
        // If we clicked directly on the overlay (not on the popup content), close it
        if (compareOverlay && comparePopup && 
            event.target === compareOverlay && 
            !comparePopup.contains(event.target)) {
          this.showCompareReport = false;
        }
      }
    }
  }
}
</script>

<style scoped>
/* Beach Search Styles */
.beach-search-container {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0.75rem;
  padding: 1rem 1rem;
  margin-top: 0.25rem;
  backdrop-filter: blur(5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  width: 100%;
  border: 1px solid rgba(255, 255, 255, 0.1);
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
}

.option-header {
  margin-bottom: 0.5rem;
  text-align: center;
  max-width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.option-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #f39c12;
  margin-bottom: 0.5rem;
}

.option-description {
  font-size: 1.2rem;
  line-height: 1.4;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.tab-buttons {
  display: flex;
  margin-bottom: 0.75rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  width: 100%;
  max-width: 98%;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
}

.tab-button {
  padding: 0.6rem 1.75rem;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 1.2rem;
  transition: all 0.3s ease;
  position: relative;
  margin: 0 0.5rem;
}

.tab-button.active {
  color: #ffffff;
}

.tab-button.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #f39c12;
}

.search-input-container {
  position: relative;
  margin-bottom: 0.75rem;
  max-width: 60%;
  margin-left: auto;
  margin-right: auto;
}

.search-input {
  width: 100%;
  padding: 1rem 1.25rem;
  border-radius: 0.5rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  background: rgba(0, 0, 0, 0.3);
  color: white;
  font-size: 1.1rem;
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.suggestions-list {
  position: absolute;
  width: 100%;
  max-height: 200px;
  overflow-y: auto;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 0.5rem;
  margin-top: 0.25rem;
  z-index: 10;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.suggestion-item {
  padding: 0.75rem 1rem;
  cursor: pointer;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  transition: background 0.2s ease;
}

.suggestion-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.loading-message {
  color: #3498db;
  margin: 1.5rem auto;
  font-weight: 600;
  text-align: center;
  max-width: 90%;
  background: rgba(52, 152, 219, 0.2);
  padding: 1.5rem;
  border-radius: 0.5rem;
  animation: pulse 1.5s infinite;
  border: 1px solid rgba(52, 152, 219, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.loading-details {
  font-size: 0.9rem;
  opacity: 0.8;
  margin-top: 0.5rem;
  font-weight: normal;
}

.loading-spinner {
  border: 5px solid rgba(52, 152, 219, 0.3);
  border-radius: 50%;
  border-top: 5px solid #3498db;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-message {
  color: #e74c3c;
  margin: 1rem auto;
  font-weight: 500;
  text-align: center;
  max-width: 90%;
  background: rgba(231, 76, 60, 0.1);
  padding: 1rem;
  border-radius: 0.5rem;
  border: 1px solid rgba(231, 76, 60, 0.3);
}

/* Modern Beach Safety Report Design */
.beach-safety-report {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1.5rem;
  padding: 0;
  margin: 1rem auto;
  max-width: 80%;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.report-header {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7));
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.report-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #f39c12;
  margin: 0;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

/* Safety Rating Card */
.safety-rating {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 0.5rem 1.25rem;
  margin: 0.5rem auto;
  max-width: 50%;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.safety-rating h4 {
  font-size: 1.1rem;
  margin: 0;
  color: #ffffff;
  flex-shrink: 0;
}

.rating-indicator {
  display: inline-block;
  padding: 0.4rem 1.25rem;
  border-radius: 2rem;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.rating-high {
  background: rgba(231, 76, 60, 0.15);
  border: 2px solid #e74c3c;
  color: #e74c3c;
}

.rating-moderate {
  background: rgba(230, 126, 34, 0.15);
  border: 2px solid #e67e22;
  color: #e67e22;
}

.rating-low {
  background: rgba(46, 204, 113, 0.15);
  border: 2px solid #2ecc71;
  color: #2ecc71;
}

.rating-unknown {
  background: rgba(149, 165, 166, 0.15);
  border: 2px solid #95a5a6;
  color: #95a5a6;
}

.rating-description {
  font-size: 1.1rem;
  line-height: 1.6;
  max-width: 90%;
  margin: 0 auto;
  color: rgba(255, 255, 255, 0.9);
}

.report-content {
  padding: 0.25rem 2rem 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}

.report-section-header {
  text-align: center;
  margin-bottom: 1rem;
  position: sticky;
  top: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  z-index: 2;
  border-radius: 0.75rem 0.75rem 0 0;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  padding: 0.25rem 0;
}

/* Condition Cards */
.condition-section {
  padding: 0.25rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.section-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0.25rem 0 0.25rem 0;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  padding: 0.25rem 0;
  max-width: 90%;
  margin-left: auto;
  margin-right: auto;
}

.compact-title {
  font-size: 1.15rem;
  white-space: nowrap;
  letter-spacing: -0.01em;
  text-transform: uppercase;
  padding: 0.3rem 0.5rem;
  background: rgba(243, 156, 18, 0.15);
  border-radius: 4px;
  display: inline-block;
}

.condition-breakdown {
  display: flex;
  gap: 1rem;
  margin-bottom: 0;
  padding: 0 1rem;
  flex: 1;
  overflow: hidden;
}

.condition-item {
  background: linear-gradient(135deg, rgba(20, 30, 48, 0.7), rgba(36, 59, 85, 0.8));
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(100, 180, 255, 0.15);
  transition: all 0.3s ease;
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  min-height: 0;
  max-height: 100%;
  margin-bottom: 0.5rem;
  overflow: hidden;
}

.condition-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
  border-color: rgba(243, 156, 18, 0.5);
}

.condition-item:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 5px;
  background: linear-gradient(to right, #f39c12, rgba(243, 156, 18, 0.5));
}

.condition-header {
  background: rgba(0, 20, 40, 0.5);
  padding: 0.4rem 0.75rem;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(100, 180, 255, 0.1);
}

.condition-icon {
  font-size: 1.8rem;
  margin-right: 0.75rem;
  width: 35px;
  height: 35px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

.condition-title {
  flex: 1;
  text-align: center;
}

.condition-name {
  display: block;
  font-weight: 700;
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 0.1rem;
}

.condition-value {
  display: block;
  font-weight: 700;
  font-size: 1.4rem;
  color: #f39c12;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.condition-meaning {
  display: flex;
  flex-direction: column;
  padding: 0;
  background: rgba(15, 25, 40, 0.5);
  padding-bottom: 0;
  margin-bottom: 0;
}

.condition-for-group {
  padding: 1rem;
  flex: 1;
}

.condition-for-group:first-child {
  border-bottom: 1px solid rgba(100, 180, 255, 0.1);
  background: rgba(0, 0, 0, 0.15);
}

.condition-for-group h5 {
  font-size: 1.15rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0 0 0.75rem 0;
  display: flex;
  align-items: center;
}

.condition-for-group h5:before {
  content: "👶";
  margin-right: 0.5rem;
}

.condition-for-group:nth-child(2) h5:before {
  content: "👤";
}

.condition-for-group ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.condition-for-group li {
  position: relative;
  padding-left: 1rem;
  margin-bottom: 0.75rem;
  line-height: 1.5;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
}

.condition-for-group li:before {
  content: "•";
  position: absolute;
  left: 0;
  color: #f39c12;
}

.condition-for-group li strong {
  color: #f39c12;
  font-weight: 600;
}

/* Family Suitability Card */
.swim-suitability {
  background: linear-gradient(135deg, rgba(15, 25, 40, 0.7), rgba(30, 40, 60, 0.8));
  border-radius: 1rem;
  overflow: hidden;
  margin-bottom: 2rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(100, 180, 255, 0.15);
  position: relative;
}

.swim-suitability:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 5px;
  background: linear-gradient(to right, #f39c12, rgba(243, 156, 18, 0.5));
}

.swim-suitability h4 {
  font-size: 1.4rem;
  margin: 0;
  color: #ffffff;
  text-align: center;
  background: rgba(0, 20, 40, 0.6);
  padding: 1.5rem;
  border-bottom: 1px solid rgba(100, 180, 255, 0.1);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.swim-guide-intro {
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 0 0 1rem 1rem;
  margin-bottom: 2rem;
  font-size: 1.1rem;
  line-height: 1.5;
}

.swim-guide-intro p {
  margin: 0;
  color: #f8f9fa;
}

.swim-guide-footer {
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 1rem;
  text-align: center;
  margin-top: 2rem;
  font-size: 0.95rem;
  line-height: 1.5;
  border-left: 4px solid #f39c12;
}

.swim-guide-footer p {
  margin: 0;
  color: #f8f9fa;
}

.suitability-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.suitability-table th {
  padding: 1rem 1.5rem;
  text-align: left;
  font-weight: 600;
  color: #f39c12;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(0, 10, 30, 0.3);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  font-size: 1.1rem;
}

.suitability-table td {
  padding: 1rem 1.5rem;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.suitability-table tbody tr:nth-child(odd) {
  background: rgba(0, 0, 0, 0.15);
}

.suitability-table tr:hover {
  background-color: rgba(243, 156, 18, 0.1) !important;
  transition: background-color 0.3s ease;
}

.suitability-table tr:last-child td {
  border-bottom: none;
}

.safety-safe {
  color: #2ecc71;
  font-weight: 700;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  text-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
  font-size: 1.5rem;
  padding-right: 15px;
}

.safety-caution {
  color: #f39c12;
  font-weight: 700;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  text-shadow: 0 0 10px rgba(243, 156, 18, 0.5);
  font-size: 1.5rem;
  padding-right: 15px;
}

.safety-not-safe {
  color: #e74c3c;
  font-weight: 700;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  text-shadow: 0 0 10px rgba(231, 76, 60, 0.5);
  font-size: 1.5rem;
  padding-right: 15px;
}

/* Key Advice Card */
.key-advice {
  background: rgba(243, 156, 18, 0.1);
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.key-advice h4 {
  font-size: 1.4rem;
  margin: 0;
  color: #ffffff;
  text-align: center;
  background: rgba(243, 156, 18, 0.2);
  padding: 1rem;
  border-bottom: 1px solid rgba(243, 156, 18, 0.3);
}

.advice-list {
  list-style-type: none;
  padding: 1.5rem 2.5rem;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
}

.advice-list li {
  position: relative;
  padding: 1rem 1rem 1rem 3rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
  line-height: 1.5;
  transition: all 0.2s ease;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.advice-list li:hover {
  background: rgba(0, 0, 0, 0.3);
  transform: translateY(-2px);
}

.advice-list li:before {
  content: "→";
  position: absolute;
  left: 1rem;
  top: 1rem;
  color: #f39c12;
  font-weight: bold;
  font-size: 1.2rem;
}

@media (max-width: 992px) {
  .condition-breakdown {
    grid-template-columns: 1fr;
    padding: 0 0.5rem;
  }
  
  .advice-list {
    grid-template-columns: 1fr;
    padding: 1rem;
  }
  
  .condition-meaning {
    flex-direction: column;
  }
}

@media (max-width: 768px) {
  .beach-safety-report {
    padding: 0;
    max-width: 100%;
  }
  
  .report-content {
    padding: 0 1rem 1.5rem;
  }
  
  .report-title {
    font-size: 1.2rem;
  }
  
  .safety-rating {
    padding: 1.25rem;
    margin-bottom: 1.5rem;
  }
  
  .section-title {
    font-size: 1.1rem;
  }
  
  .condition-header {
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    text-align: center;
  }
  
  .condition-icon {
    margin-right: 0;
    margin-bottom: 0.5rem;
  }
  
  .suitability-table th, 
  .suitability-table td {
    padding: 0.75rem;
    font-size: 0.9rem;
  }
  
  .rating-indicator {
    padding: 0.5rem 1.5rem;
    font-size: 1.1rem;
  }
  
  .beach-search-container {
    padding: 1rem 0.75rem;
  }
  
  .tab-buttons {
    justify-content: center;
  }
  
  .tab-button {
    padding: 0.5rem 0.75rem;
    font-size: 1rem;
  }
  
  .compare-inputs {
    flex-direction: column;
    gap: 50px;
    align-items: center;
  }
  
  .compare-input-wrapper {
    width: 100%;
    max-width: 100%;
  }
  
  .beach-label {
    margin-left: 0;
  }
  
  .compare-button {
    width: 80%;
  }
  
  .compare-tab .suggestions-list {
    width: 100%;
    left: 0;
  }
  
  .report-tabs {
    flex-wrap: wrap;
  }
  
  .report-tab {
    padding: 0.75rem 0.25rem;
    font-size: 0.8rem;
  }
  
  .beach-comparison {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .chart-container {
    padding: 1rem;
    max-width: 95%;
  }
}

@media (max-width: 480px) {
  .beach-search-container {
    padding: 0.75rem 0.5rem;
  }
  
  .tab-buttons {
    margin-bottom: 1rem;
  }
  
  .tab-button {
    padding: 0.5rem 0.75rem;
    font-size: 0.8rem;
  }
  
  .option-title {
    font-size: 1rem;
  }
  
  .option-description {
    font-size: 0.85rem;
  }
  
  .condition-icon {
    font-size: 1.8rem;
  }
  
  .condition-value {
    font-size: 1.3rem;
  }
  
  .compare-button {
    width: 70%;
    padding: 0.6rem 1rem;
    font-size: 1rem;
  }
}

/* Compare tab styles */
.compare-wrapper {
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
}

.compare-inputs {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 1.5rem;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  margin-top: 0.5rem;
  transition: all 0.3s ease-in-out;
}

.compare-inputs-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 30px;
  width: 100%;
}

.suggestions-row {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  width: 100%;
  margin-top: 5px;
  min-height: 50px;
}

.suggestions-column {
  flex: 1;
  opacity: 0.5;
  transition: all 0.3s ease;
}

.suggestions-column.active {
  opacity: 1;
}

.expanded .compare-inputs {
  padding: 1.5rem 1.5rem 2rem 1.5rem;
  background: rgba(0, 0, 0, 0.3);
}

/* Mobile styles for compare beaches section */
@media (max-width: 768px) {
  .compare-inputs-row {
    flex-direction: column;
    gap: 20px;
    align-items: center;
  }
  
  .compare-input-wrapper {
    max-width: 100%;
    width: 100%;
  }
  
  .suggestions-row {
    flex-direction: column;
    gap: 15px;
  }
  
  .suggestions-column {
    opacity: 1;
  }
  
  .compare-wrapper.expanded {
    min-height: 350px;
    padding-bottom: 20px;
  }
  
  .compare-button {
    margin-top: 25px;
    width: 80%;
  }
}

.compare-input-wrapper {
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 70px;
  max-width: 48%;
  width: 100%;
}

.beach-label {
  background: #f39c12;
  color: white;
  padding: 0.5rem 1.5rem;
  border-radius: 0.5rem 0.5rem 0 0;
  font-weight: 600;
  text-align: center;
  width: fit-content;
  margin: 0;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.3);
}

.compare-input-container {
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0 0.5rem 0.5rem 0.5rem;
  padding: 0.5rem 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  width: 100%;
  height: 100%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  z-index: 999; /* Increased z-index to ensure proper stacking but lower than suggestions */
}

.compare-button-container {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-top: 15px;
  transition: margin 0.3s ease;
  position: relative;
  z-index: 10;
}

.compare-button-container.has-suggestions {
  margin-top: 25px;
}

.compare-button {
  width: 50%;
  margin: 0 auto;
  padding: 0.6rem;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  cursor: pointer;
  border: none;
  border-radius: 0.5rem;
  background: linear-gradient(135deg, #f39c12, #e67e22);
  color: white;
  font-weight: 600;
  transition: all 0.3s ease;
  animation: pulse 2s infinite ease-in-out;
  box-shadow: 0 4px 15px rgba(243, 156, 18, 0.4);
  position: relative;
  z-index: 5;
}

@media (max-width: 768px) {
  .compare-inputs {
    flex-direction: column;
    gap: 30px;
    padding: 1.2rem;
  }
  
  .compare-tab .suggestions-list {
    width: 100%;
    left: 0;
  }
  
  .compare-input-wrapper {
    width: 100%;
    max-width: 100%;
    height: auto;
    margin-bottom: 5px;
  }
  
  .compare-input-container {
    height: 70px;
  }
  
  .beach-label {
    margin-left: 0;
  }
  
  .compare-button {
    width: 80%;
    margin: 10px auto 0;
  }
}

.compare-tab .search-input {
  width: 100%;
  height: 100%;
  padding: 0 1rem 0 3.5rem;
  border-radius: 0.5rem;
  border: none;
  background: transparent;
  color: white;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  outline: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.compare-tab .search-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.input-icon {
  position: absolute;
  top: 50%;
  left: 1rem;
  transform: translateY(-50%);
  font-size: 1.8rem;
  color: rgba(255, 255, 255, 0.8);
  z-index: 1;
}

.compare-button:hover {
  background: #e67e22;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

.compare-button:disabled {
  background: #95a5a6;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.7;
}

.compare-tab .suggestions-list {
  position: absolute;
  width: 110%;
  max-height: 300px;
  overflow-y: auto;
  background: rgba(0, 0, 0, 0.95);
  border-radius: 0.7rem;
  margin-top: 0.6rem;
  z-index: 9999; /* Significantly increased z-index to ensure it appears on top */
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(243, 156, 18, 0.3);
  left: -5%;
  top: 100%; /* Position it directly below the input */
}

.compare-tab .suggestion-item {
  padding: 1rem 1.5rem;
  cursor: pointer;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  transition: all 0.2s ease;
  white-space: normal;
  overflow: visible;
  text-overflow: clip;
  line-height: 1.4;
  font-size: 1rem;
  word-wrap: break-word;
  position: relative;
}

.compare-tab .suggestion-item:hover {
  background: rgba(243, 156, 18, 0.2);
}

.compare-tab .suggestion-item:last-child {
  border-bottom: none;
}

.compare-tab .suggestion-item:before {
  content: '🔍';
  margin-right: 0.5rem;
  opacity: 0.7;
}

.comparison-chart-area {
  width: 95%;
  margin: 2rem auto;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
}

.chart-title {
  text-align: center;
  font-size: 1.5rem;
  font-weight: 700;
  color: #f39c12;
  margin-bottom: 0.75rem;
}



.safety-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.beach-safety-column {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.beach-safety-name {
  text-align: center;
  font-size: 1.4rem;
  font-weight: 700;
  color: #f39c12;
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.safety-factor {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1.25rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.factor-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
}

.factor-icon {
  font-size: 1.75rem;
  margin-right: 0.75rem;
}

.factor-title {
  flex: 1;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
}

.factor-explanation {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.5;
  margin: 0;
}

.risk-high {
  background-color: rgba(231, 76, 60, 0.2);
  color: #e74c3c;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.95rem;
  border: 1px solid rgba(231, 76, 60, 0.5);
}

.risk-moderate {
  background-color: rgba(243, 156, 18, 0.2);
  color: #f39c12;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.95rem;
  border: 1px solid rgba(243, 156, 18, 0.5);
}

.risk-low {
  background-color: rgba(46, 204, 113, 0.2);
  color: #2ecc71;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-weight: 600;
  font-size: 0.95rem;
  border: 1px solid rgba(46, 204, 113, 0.5);
}

.chart-container {
  background: rgba(0, 0, 0, 0.5);
  border-radius: 0.75rem;
  padding: 1.5rem;
  max-width: 95%;
  margin: 0 auto 2rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(243, 156, 18, 0.4);
}

.chart-footer {
  text-align: center;
  font-size: 0.9rem;
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  font-style: italic;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.beach-column {
  flex: 1;
  text-align: center;
}

.beach-comparison {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 95%;
  margin: 0 auto;
}

.beach-comparison-column {
  flex: 1;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.comparison-data {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.comparison-row {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.comparison-label {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.comparison-bar-container {
  height: 1.25rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3);
}

.comparison-bar {
  height: 100%;
  transition: width 0.8s ease;
  border-radius: 1rem;
  animation: fadeInBar 1s ease-out forwards;
}

@keyframes fadeInBar {
  from { width: 0; opacity: 0.3; }
  to { opacity: 1; }
}

.comparison-value {
  position: absolute;
  right: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.85rem;
  color: white;
  font-weight: 600;
  text-shadow: 0 0 4px rgba(0, 0, 0, 1);
}

.beach-name {
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0.5rem 0;
  padding: 0.75rem 1.25rem;
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 0.6rem;
  display: inline-block;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  color: #f39c12;
  border: 1px solid rgba(243, 156, 18, 0.3);
  letter-spacing: 0.5px;
}

.status-message {
  background: rgba(34, 139, 230, 0.2);
  color: #3498db;
  padding: 1rem;
  border-radius: 0.5rem;
  text-align: center;
  margin: 1rem auto;
  width: 90%;
  border: 1px solid rgba(52, 152, 219, 0.3);
  font-weight: 500;
}

.debug-message {
  background: rgba(243, 156, 18, 0.2);
  color: #f39c12;
  padding: 1rem;
  border-radius: 0.5rem;
  text-align: center;
  margin: 1rem auto;
  width: 90%;
  border: 1px solid rgba(243, 156, 18, 0.3);
  font-weight: 500;
}

/* Beach Condition Category Styles */
.beach-condition-category {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 0.8rem;
  padding: 0.7rem;
  margin-bottom: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  height: auto;
  min-height: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.category-badge {
  font-size: 1.3rem;
  font-weight: 800;
  display: inline-block;
  padding: 0.5rem 2rem;
  border-radius: 2rem;
  margin: 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
  letter-spacing: 2px;
  text-align: center;
  min-width: 150px;
  text-transform: uppercase;
}

.category-explanation {
  font-size: 0.9rem;
  line-height: 1.4;
  margin: 0;
}

.category-harsh {
  background: rgba(231, 76, 60, 0.15);
  border: 1px solid rgba(231, 76, 60, 0.5);
  margin-left: auto;
  margin-right: auto;
}

.category-harsh .category-badge {
  background: #e74c3c;
  color: white;
}

.category-harsh .category-explanation {
  color: rgba(255, 255, 255, 0.9);
}

.category-moderate {
  background: rgba(243, 156, 18, 0.15);
  border: 1px solid rgba(243, 156, 18, 0.5);
  margin-left: auto;
  margin-right: auto;
}

.category-moderate .category-badge {
  background: #f39c12;
  color: white;
}

.category-moderate .category-explanation {
  color: rgba(255, 255, 255, 0.9);
}

.category-calm {
  background: rgba(46, 204, 113, 0.15);
  border: 1px solid rgba(46, 204, 113, 0.5);
  margin-left: auto;
  margin-right: auto;
}

.category-calm .category-badge {
  background: #2ecc71;
  color: white;
}

.category-calm .category-explanation {
  color: rgba(255, 255, 255, 0.9);
}

/* Comparison Tabs Styles */
.comparison-tabs {
  display: flex;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 2rem;
  position: sticky;
  top: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  z-index: 2;
  border-radius: 1rem 1rem 0 0;
}

.comparison-tab {
  flex: 1;
  text-align: center;
  padding: 1rem;
  cursor: pointer;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
  position: relative;
}

.comparison-tab.active {
  color: #f39c12;
}

.comparison-tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #f39c12;
}

/* Recommendation Tab Styles */
.recommendation-tab {
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  margin-bottom: 2rem;
}

.beach-recommendation-cards {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: 2rem;
}

.recommendation-card {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 1rem;
  padding: 1.5rem;
  flex: 1;
  text-align: left;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.recommendation-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
}

.recommendation-card.category-harsh {
  background: linear-gradient(135deg, rgba(30, 10, 10, 0.7), rgba(50, 15, 15, 0.8));
  border-color: rgba(231, 76, 60, 0.3);
}

.recommendation-card.category-moderate {
  background: linear-gradient(135deg, rgba(40, 30, 10, 0.7), rgba(60, 45, 15, 0.8));
  border-color: rgba(243, 156, 18, 0.3);
}

.recommendation-card.category-calm {
  background: linear-gradient(135deg, rgba(10, 30, 20, 0.7), rgba(15, 50, 30, 0.8));
  border-color: rgba(46, 204, 113, 0.3);
}

.beach-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #f39c12;
  margin: 0.3rem 0 0.75rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 0.5rem;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.beach-category {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
  text-align: center;
}

.category-badge {
  font-size: 1.1rem;
  font-weight: 800;
  display: inline-block;
  padding: 0.25rem 1.5rem;
  border-radius: 2rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  letter-spacing: 1px;
  text-align: center;
  min-width: 120px;
}

.beach-summary {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 1.5rem;
  overflow: visible;
}

.summary-intro {
  font-size: 1.1rem;
  margin-bottom: 1.2rem;
  font-weight: 500;
  color: #fff;
  text-align: center;
}

/* Adjust key dangers to look better */
.key-dangers {
  margin-top: 1rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

.danger-card {
  background: rgba(0, 0, 0, 0.25);
  border-radius: 0.6rem;
  padding: 0.85rem;
  display: flex;
  gap: 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.danger-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  border-color: rgba(243, 156, 18, 0.4);
}

.danger-icon {
  font-size: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  opacity: 0.9;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  flex-shrink: 0;
}

.danger-content {
  flex: 1;
}

.danger-title {
  color: #f39c12;
  margin: 0 0 0.5rem;
  font-size: 1rem;
  font-weight: 700;
  border-bottom: 1px solid rgba(243, 156, 18, 0.3);
  padding-bottom: 0.3rem;
}

.danger-impacts {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.impact-group {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.impact-label {
  color: rgba(255, 255, 255, 0.9);
  font-weight: 600;
  font-size: 0.85rem;
}

.impact-text {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  line-height: 1.4;
}

.recommendation-label {
  font-size: 1.1rem;
  font-weight: 600;
  color: #f39c12;
  margin: 1rem 0 0.5rem;
}

.best-for-groups {
  font-size: 1rem;
  line-height: 1.5;
  color: white;
  font-weight: 600;
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 0.5rem;
  background: rgba(0, 0, 0, 0.2);
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.beach-advice {
  margin-top: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.beach-advice h5 {
  font-size: 1.1rem;
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 0.75rem;
}

.beach-advice ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.beach-advice li {
  margin-bottom: 0.75rem;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
  padding-left: 1.5rem;
  position: relative;
  line-height: 1.4;
}

.beach-advice li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #f39c12;
  font-weight: bold;
}

.beach-advice li:last-child {
  margin-bottom: 0;
}

.comparison-conclusion {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 1.5rem;
  margin-top: 1rem;
  border: 1px solid rgba(243, 156, 18, 0.2);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.conclusion-horizontal {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.conclusion-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0;
  padding: 0;
  border: none;
  flex: 1;
  text-align: left;
}

.conclusion-body {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  text-align: center;
}

.readiness-status {
  font-size: 1.8rem;
  font-weight: 700;
  text-align: right;
  margin: 0;
  padding: 0 1rem;
  color: #f8f9fa;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  min-width: 180px;
}

/* Beach image styles */
.beach-image-container {
  width: 100%;
  height: 140px;
  overflow: hidden;
  border-radius: 0.5rem;
  margin-bottom: 0.75rem;
  position: relative;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.beach-condition-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.recommendation-card:hover .beach-condition-image {
  transform: scale(1.05);
}

.beach-image-container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.5));
  pointer-events: none;
}

.category-harsh .beach-image-container::after {
  background: linear-gradient(to bottom, rgba(231, 76, 60, 0.1), rgba(0, 0, 0, 0.5));
}

.category-moderate .beach-image-container::after {
  background: linear-gradient(to bottom, rgba(243, 156, 18, 0.1), rgba(0, 0, 0, 0.5));
}

.category-calm .beach-image-container::after {
  background: linear-gradient(to bottom, rgba(46, 204, 113, 0.1), rgba(0, 0, 0, 0.5));
}

/* Beach type ribbon */
.beach-type-ribbon {
  position: absolute;
  top: 15px;
  right: -5px;
  background: #f39c12;
  color: white;
  padding: 0.4rem 1rem;
  font-weight: 600;
  font-size: 0.9rem;
  z-index: 2;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  border-radius: 0.3rem 0 0 0.3rem;
}

.beach-type-ribbon:before {
  content: '';
  position: absolute;
  right: 0;
  bottom: -5px;
  border-top: 5px solid #c48009;
  border-right: 5px solid transparent;
}

@media (min-width: 992px) {
  .key-dangers {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .danger-card {
    flex-direction: row;
    align-items: flex-start;
  }
  
  .danger-icon {
    margin-top: 0.25rem;
  }
  
  .beach-image-container {
    height: 200px;
  }
  
  .beach-category {
    justify-content: center;
  }
  
  .category-badge {
    margin-left: 0;
  }
}

.beach-comparison-cards {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: 2rem;
  align-items: flex-start; /* Changed from stretch to align at the top */
}

@media (max-width: 768px) {
  .beach-comparison-cards {
    flex-direction: column;
    gap: 2rem;
  }
  }
  
.beach-comparison-card {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 1rem;
  padding: 1rem 1.5rem;
  flex: 1;
  text-align: left;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 580px;
  max-width: 500px;
  margin: 0 auto;
}

.beach-comparison-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
}

.beach-comparison-card.category-harsh {
  background: linear-gradient(135deg, rgba(30, 10, 10, 0.7), rgba(50, 15, 15, 0.8));
  border-color: rgba(231, 76, 60, 0.3);
}

.beach-comparison-card.category-moderate {
  background: linear-gradient(135deg, rgba(40, 30, 10, 0.7), rgba(60, 45, 15, 0.8));
  border-color: rgba(243, 156, 18, 0.3);
  }
  
.beach-comparison-card.category-calm {
  background: linear-gradient(135deg, rgba(10, 30, 20, 0.7), rgba(15, 50, 30, 0.8));
  border-color: rgba(46, 204, 113, 0.3);
}

.beach-condition-category {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 0.8rem;
  padding: 1rem;
  margin-bottom: 1.2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  height: auto;
  min-height: 70px;
  display: flex;
    flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.category-badge {
  font-size: 2.6rem;
  font-weight: 900;
  display: inline-block;
  padding: 0.5rem 1.5rem;
  margin: 0 auto;
  letter-spacing: 3px;
  text-align: center;
  text-transform: uppercase;
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
  animation: glow 2s infinite alternate;
}

.category-harsh .category-badge {
  color: #ff5a4a;
  text-shadow: 0 2px 5px rgba(231, 76, 60, 0.7);
}

.category-moderate .category-badge {
  color: #ffae30;
  text-shadow: 0 2px 5px rgba(243, 156, 18, 0.7);
}

.category-calm .category-badge {
  color: #46e88c;
  text-shadow: 0 2px 5px rgba(46, 204, 113, 0.7);
}

.beach-condition-category {
  margin-bottom: 1.2rem;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.category-explanation {
  font-size: 0.95rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.95);
  margin-top: 0.5rem;
  width: 100%;
}

.beach-comparison-card {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 1rem;
  padding: 1rem 1.5rem;
  flex: 1;
  text-align: left;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 580px;
  max-width: 500px;
  margin: 0 auto;
}

.beach-comparison-cards {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: 2rem;
  align-items: flex-start;
}

@media (max-width: 768px) {
  .beach-comparison-cards {
    flex-direction: column;
    gap: 2rem;
  }
  
  .beach-comparison-card {
    width: 100%;
    min-height: 600px;
  }
  
  .beach-condition-category {
    margin-bottom: 1rem;
  }
  
  .beach-report-popup {
    height: 85vh;
    max-height: 85vh;
    width: 98%;
    padding: 0;
  }
  
  .report-content {
    padding: 0.25rem 1rem 1rem;
  }
}

.detailed-tab {
  padding: 1rem 0;
}

.beach-differences {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 1rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.differences-title {
  text-align: center;
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 1rem;
}

.differences-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.difference-item {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.difference-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

.difference-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  gap: 1rem;
}

.difference-icon {
  font-size: 1.75rem;
  flex-shrink: 0;
}

.difference-title {
  margin: 0;
  font-size: 1.2rem;
  color: white;
}

.difference-body {
  padding: 1rem;
}

.difference-description {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0 0 1rem;
  color: rgba(255, 255, 255, 0.9);
}

.difference-impact {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
  padding: 0.75rem;
  border-radius: 0.5rem;
  background: rgba(0, 0, 0, 0.15);
  color: rgba(255, 255, 255, 0.95);
}

.difference-impact strong {
  color: #f39c12;
}

.beach-similarities {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 1rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.similarities-title {
  text-align: center;
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 1rem;
}

.similarities-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.similarity-item {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.similarity-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

.similarity-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  gap: 1rem;
}

.similarity-icon {
  font-size: 1.75rem;
  flex-shrink: 0;
}

.similarity-title {
  margin: 0;
  font-size: 1.2rem;
  color: white;
}

.similarity-body {
  padding: 1rem;
}

.similarity-description {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0 0 1rem;
  color: rgba(255, 255, 255, 0.9);
}

.similarity-impact {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
  padding: 0.75rem;
  border-radius: 0.5rem;
  background: rgba(0, 0, 0, 0.15);
  color: rgba(255, 255, 255, 0.95);
}

.similarity-impact strong {
  color: #f39c12;
}

.severity-high {
  border-left: 4px solid #e74c3c;
}

.severity-high .difference-header,
.severity-high .similarity-header {
  background: rgba(231, 76, 60, 0.1);
}

.severity-high .difference-title,
.severity-high .similarity-title {
  color: #e74c3c;
}

.severity-moderate {
  border-left: 4px solid #f39c12;
}

.severity-moderate .difference-header,
.severity-moderate .similarity-header {
  background: rgba(243, 156, 18, 0.1);
}

.severity-moderate .difference-title,
.severity-moderate .similarity-title {
  color: #f39c12;
}

.severity-low {
  border-left: 4px solid #2ecc71;
}

.severity-low .difference-header,
.severity-low .similarity-header {
  background: rgba(46, 204, 113, 0.1);
}

.severity-low .difference-title,
.severity-low .similarity-title {
  color: #2ecc71;
}

/* Add CSS for the no-comparison-data message */
.no-comparison-data {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
  margin: 2rem auto;
  max-width: 80%;
}

.no-comparison-data h3 {
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.no-comparison-data p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.differences-intro, .similarities-intro {
  text-align: center;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 1.5rem;
  font-size: 1.1rem;
  line-height: 1.4;
  font-style: italic;
}

.full-width {
  grid-column: 1 / -1;
}

@media (max-width: 992px) {
  .safety-comparison {
    grid-template-columns: 1fr;
  }
  
  .beach-differences, .beach-similarities, .full-width {
    grid-column: 1;
  }
}

/* Add CSS for the warning message */
.same-beach-warning {
  margin: 1rem auto;
  padding: 1rem;
  background: rgba(231, 76, 60, 0.2);
  border: 1px solid rgba(231, 76, 60, 0.4);
  border-radius: 0.5rem;
  color: white;
  font-weight: 500;
  text-align: center;
  max-width: 80%;
  animation: fadeIn 0.3s ease-in-out;
}

.same-beach-warning div {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.warning-icon {
  font-size: 1.4rem;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.risk-meter-container {
  position: relative;
  width: 95%;
  margin: 5px auto 10px;
  padding: 2px 0 15px;
}

.risk-meter-title {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 6px;
  text-align: center;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.risk-meter {
  position: relative;
  height: 22px;
  background: rgba(0, 0, 0, 0.4);
  border-radius: 11px;
  overflow: visible;
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4);
}

.risk-segments {
  display: flex;
  width: 100%;
  height: 100%;
  border-radius: 11px;
  overflow: hidden;
}

.risk-segment {
  height: 100%;
  flex: 1;
  position: relative;
}

.risk-segment:after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  height: 100%;
  width: 2px;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 2;
}

.risk-segment:last-child:after {
  display: none;
}

.risk-segment.safe {
  background: linear-gradient(to bottom, #2ecc71, #27ae60);
}

.risk-segment.caution {
  background: linear-gradient(to bottom, #f39c12, #e67e22);
}

.risk-segment.danger {
  background: linear-gradient(to bottom, #e74c3c, #c0392b);
}

.risk-indicator {
  position: absolute;
  top: -10px;
  transform: translateX(-50%);
  width: 24px;
  height: 40px;
  transition: left 0.5s ease;
  z-index: 5;
}

.risk-indicator:before {
  content: '';
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  width: 24px;
  height: 24px;
  background-color: white;
  border: 3px solid #333;
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
  z-index: 5;
  animation: pulse 1.5s infinite;
}

.risk-indicator-arrow {
  display: none; /* Hide the triangle arrow */
  position: relative;
  width: 0;
  height: 0;
  margin: 0 auto;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 16px solid #333;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.4));
  z-index: 6;
}

.risk-value {
  display: none; /* Hide the numerical value */
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
  }
}

.risk-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
  font-size: 1.1rem;
  font-weight: 700;
  padding: 0 10px;
  color: rgba(255, 255, 255, 0.95);
}

.risk-label.safe {
  color: #2ecc71;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
  font-weight: 800;
}

.risk-label.caution {
  color: #f39c12;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
  font-weight: 800;
}

.risk-label.danger {
  color: #e74c3c;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
  font-weight: 800;
}

.wave-danger-visual {
  position: relative;
  width: 100%;
  margin-bottom: 0;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  cursor: pointer;
}

.wave-danger-image {
  width: 100%;
  height: 140px;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
  margin-bottom: 0;
}

.wave-danger-visual:hover .wave-danger-image {
  transform: scale(1.05);
}

.wave-danger-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  transition: opacity 0.3s ease;
  opacity: 1;
  padding-bottom: 15px;
}

.wave-danger-visual:hover .wave-danger-overlay {
  opacity: 0;
}

.wave-danger-overlay.moderate {
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.6));
}

.wave-danger-overlay.safe {
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.6));
}

.hover-prompt {
  position: relative;
  bottom: 0;
  text-align: center;
  background-color: rgba(0, 0, 0, 0.7);
  padding: 8px 12px;
  border-radius: 20px;
  margin: 0 auto;
  width: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pulse-opacity 2s infinite;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
}

.danger-text {
  color: white;
  font-size: 1.75rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  margin-bottom: 0.5rem;
}

.hover-description {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
  overflow: hidden;
}

.wave-danger-visual:hover .hover-description {
  opacity: 1;
}

.hover-content {
  padding: 1rem;
  color: white;
  text-align: center;
  max-width: 90%;
  font-size: 0.95rem;
  line-height: 1.3;
}

.hover-content h4 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  font-weight: 700;
  color: #f39c12;
}

.hover-content p {
  margin-bottom: 0.75rem;
  line-height: 1.4;
}

.wave-visual-header {
  font-size: 0.95rem;
  font-weight: 600;
  color: #f39c12;
  margin-bottom: 0.1rem;
  text-align: center;
  position: relative;
  z-index: 1;
  padding: 0.1rem;
}

@keyframes point-up {
  from { transform: translateY(3px); }
  to { transform: translateY(-2px); }
}

@keyframes pulse-opacity {
  0% { opacity: 0.7; }
  50% { opacity: 1; }
  100% { opacity: 0.7; }
}

.wave-danger-visual {
  position: relative;
  width: 100%;
  margin-bottom: 0;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  cursor: pointer;
}

.hover-icon {
  font-size: 1.2rem;
  margin-right: 8px;
  animation: point-up 1s ease-in-out infinite alternate;
}

.hover-text {
  font-size: 0.85rem;
  color: white;
  font-weight: 500;
}

.visual-comparison-container {
  margin-top: 2rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
}

.visual-comparison-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #f39c12;
  margin-bottom: 1rem;
  text-align: center;
}

.visual-comparison {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.comparison-item {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.comparison-visual {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.beach-column {
  flex: 1;
  text-align: center;
}

.beach-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #f39c12;
  margin-bottom: 0.5rem;
  background-color: rgba(0, 0, 0, 0.3);
  padding: 0.3rem 0.75rem;
  border-radius: 0.3rem;
  display: inline-block;
}

.visual-image-container {
  width: 100%;
  height: 150px;
  overflow: hidden;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
  position: relative;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.condition-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.visual-image-container:hover .condition-image {
  transform: scale(1.05);
}

.comparison-arrows {
  flex: 0.7;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0.5rem;
}

.arrow-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(0, 0, 0, 0.3);
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  width: 100%;
  max-width: 200px;
  min-height: 80px;
  justify-content: center;
}

.arrow-text {
  font-size: 0.95rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.arrow {
  font-size: 2.5rem;
  line-height: 1;
}

.arrow-container.danger {
  background: rgba(231, 76, 60, 0.2);
  border: 1px solid rgba(231, 76, 60, 0.3);
}

.arrow-container.danger .arrow-text {
  color: #f1c40f;
}

.arrow-container.danger .arrow {
  color: #e74c3c;
}

.arrow-container.warning .arrow-text {
  color: #f1c40f;
}

.arrow-container.warning .arrow {
  color: #f39c12;
}

.arrow-container.safe {
  background: rgba(46, 204, 113, 0.15);
  border: 1px solid rgba(46, 204, 113, 0.3);
}

.arrow-container.safe .arrow-text {
  color: #ffffff;
}

.arrow-container.safe .arrow {
  color: #2ecc71;
}

.arrow-container.similar {
  background: rgba(52, 152, 219, 0.15);
  border: 1px solid rgba(52, 152, 219, 0.3);
}

.arrow-container.similar .arrow-text {
  color: #ffffff;
}

.arrow-similar {
  font-size: 2.5rem;
  color: #3498db;
  line-height: 1;
}

.comparison-item-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #f39c12;
  margin-bottom: 1rem;
  text-align: center;
}

.wave-size-indicator, .current-speed-indicator {
  font-size: 1.1rem;
  font-weight: 600;
  color: #f8f9fa;
  margin-top: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  display: inline-block;
}

.safety-impact-summary {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin-top: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.impact-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #f39c12;
  margin-bottom: 1rem;
  text-align: center;
}

.impact-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.impact-list li {
  display: flex;
  align-items: flex-start;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  background: rgba(0, 0, 0, 0.15);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.impact-list li.danger {
  background: rgba(231, 76, 60, 0.15);
  border-left: 4px solid #e74c3c;
}

.impact-list li.warning {
  background: rgba(243, 156, 18, 0.15);
  border-left: 4px solid #f39c12;
}

.impact-list li.info {
  background: rgba(52, 152, 219, 0.15);
  border-left: 4px solid #3498db;
}

.impact-list li.safe {
  background: rgba(46, 204, 113, 0.15);
  border-left: 4px solid #2ecc71;
}

.impact-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
  flex-shrink: 0;
}

.impact-text {
  font-size: 1rem;
  line-height: 1.4;
  flex: 1;
}

@media (max-width: 768px) {
  .comparison-visual {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .comparison-arrows {
    width: 100%;
    flex-direction: row;
    justify-content: center;
    padding: 0.5rem 0;
  }
  
  .arrow-container {
    flex-direction: row;
    max-width: 100%;
    gap: 0.5rem;
    min-height: auto;
    padding: 0.5rem;
  }
  
  .arrow-text {
    text-align: left;
    margin-bottom: 0;
    font-size: 0.9rem;
  }
  
  .arrow, .arrow-similar {
    font-size: 1.5rem;
    transform: rotate(90deg);
  }
  
  .beach-comparison-cards {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .beach-comparison-card {
    width: 100%;
  }
  
  .visual-comparison-container {
    padding: 1rem;
  }
}

.visual-wave-container {
  margin-bottom: 2rem;
  padding: 1rem;
  border-radius: 0.75rem;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  min-height: 220px;
}

.visual-wave-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #ffae30;
  margin-bottom: 0.5rem;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  letter-spacing: 0.5px;
}

.wave-visual-card, .current-visual-card {
  position: relative;
  border-radius: 0.75rem;
  overflow: hidden !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  height: 420px; /* Increased from 180px */
  margin-bottom: 0;
  contain: strict;
  max-height: 4200px; /* Increased from 180px */
}

.wave-image, .current-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  transition: transform 0.3s ease;
  min-height: 120px;
  transform-origin: center center;
}

.wave-visual-card:hover .wave-image,
.current-visual-card:hover .current-image {
  transform: scale(1.03);
}

.hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.3s ease;
  bottom: 0;
}

.hover-prompt {
  background: rgba(0, 0, 0, 0.8);
  padding: 0.6rem 1.4rem;
  border-radius: 2rem;
  color: #fff;
  font-weight: 700;
  font-size: 1rem;
  border: 2px solid rgba(243, 156, 18, 0.7);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  animation: pulse 2s infinite;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  letter-spacing: 0.5px;
  position: absolute;
  bottom: 15px;
}

@keyframes pulse {
  0% { 
    transform: scale(1); 
    box-shadow: 0 0 0 0 rgba(243, 156, 18, 0.4);
  }
  50% { 
    transform: scale(1.05); 
    box-shadow: 0 0 0 10px rgba(243, 156, 18, 0);
  }
  100% { 
    transform: scale(1); 
    box-shadow: 0 0 0 0 rgba(243, 156, 18, 0);
  }
}

.wave-details-card, .current-details-card {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding: 0.75rem;
  background: rgba(0, 0, 0, 0.95);
  border-radius: 0.75rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  opacity: 0;
  transform: translateY(0);
  transition: opacity 0.3s ease, transform 0.3s ease;
  overflow: hidden;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  bottom: 0;
  z-index: 5;
  max-height: 100%;
}

.wave-visual-card:hover .wave-details-card,
.current-visual-card:hover .current-details-card {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.wave-visual-card:hover .hover-overlay,
.current-visual-card:hover .hover-overlay {
  opacity: 0;
}

.wave-comparison, .current-comparison {
  color: rgba(255, 255, 255, 0.95);
  font-size: 1.1rem;
  line-height: 1.4;
  margin-bottom: 0;
  width: 100%;
  font-weight: 600;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.wave-comparison p, .current-comparison p {
  margin-bottom: 0.3rem;
  margin-top: 0;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.highlight {
  color: #ffae30;
  font-weight: 800;
  font-size: 1.3rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  padding: 0 2px;
}

.impact-description {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.impact-description p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  line-height: 1.5;
  margin-bottom: 0.5rem;
}

.warning-text {
  color: #e74c3c;
  font-weight: 700;
  font-size: 1.1rem;
}

.advice-text {
  color: #3498db;
  font-weight: 700;
  font-size: 1.1rem;
}

.safe-text {
  color: #2ecc71;
  font-weight: 700;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .wave-visual-card, .current-visual-card {
    height: 250px; /* This remains 250px, could be adjusted if needed */
    max-height: 250px; /* This remains 250px */
  }
  
  .wave-details-card, .current-details-card {
    font-size: 0.9rem;
    padding: 0.75rem;
  }
  
  .hover-prompt {
    font-size: 0.9rem;
    padding: 0.5rem 1rem;
  }
}

.safe-text {
  color: #2ecc71;
  font-weight: 700;
  font-size: 1.1rem;
}

.visual-current-container {
  margin-bottom: 2rem;
  padding: 1rem;
  border-radius: 0.75rem;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  min-height: 220px;
}

.visual-current-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #ffae30;
  margin-bottom: 0.5rem;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  letter-spacing: 0.5px;
}

@media (max-width: 768px) {
  .visual-current-title {
    font-size: 1rem;
    margin-bottom: 0.5rem;
  }
}

.beach-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #f39c12;
  margin: 0.3rem 0 0.75rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 0.5rem;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.beach-image-container {
  width: 100%;
  height: 140px;
  overflow: hidden;
  border-radius: 0.5rem;
  margin-bottom: 0.75rem;
  position: relative;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Style the suitability table to look better in the cards */
.best-for-groups-container {
  margin-top: auto; /* Push to bottom of card */
  padding-top: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem;
  margin-top: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) inset;
}

.suitability-wrapper {
  width: 100%;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  background-color: rgba(0, 0, 0, 0.3);
  border: 2px solid rgba(255, 255, 255, 0.15);
  margin-bottom: 0.5rem;
  background: linear-gradient(to bottom, #0a0a0a, rgba(20, 20, 20, 0.9));
}

.suitability-header {
  display: flex;
  background-color: rgba(0, 0, 0, 0.4);
  border-bottom: 2px solid rgba(255, 255, 255, 0.15);
  padding: 0.75rem 0;
}

.suitability-header-age {
  flex: 0 0 70%;
  padding-left: 1rem;
  color: #ffae30;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 1.1rem;
  text-align: left;
}

.suitability-header-safe {
  flex: 0 0 30%;
  padding-right: 2rem;
  color: #ffae30;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 1.1rem;
  text-align: right;
}

.suitability-row {
  display: flex;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  align-items: center;
}

.suitability-row:last-child {
  border-bottom: none;
}

.suitability-age {
  flex: 0 0 70%;
  padding: 0.9rem 1rem;
  font-size: 1.2rem;
  font-weight: 700;
  color: #ffffff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  text-align: left;
}

.suitability-safe {
  flex: 0 0 30%;
  padding-right: 2rem;
  font-size: 1.5rem;
  font-weight: 700;
  text-align: right;
}

.safety-safe {
  color: #2ecc71;
  text-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
}

.safety-caution {
  color: #f39c12;
  text-shadow: 0 0 10px rgba(243, 156, 18, 0.5);
}

.safety-not-safe {
  color: #e74c3c;
  text-shadow: 0 0 10px rgba(231, 76, 60, 0.5);
}

.recommendation-label {
  font-size: 1.4rem;
  font-weight: 700;
  color: #ffae30;
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.safety-safe {
  color: #2ecc71;
  font-weight: 900;
  text-shadow: 0 0 10px rgba(46, 204, 113, 0.7);
  font-size: 1.7rem;
}

.safety-caution {
  color: #f39c12;
  font-weight: 900;
  text-shadow: 0 0 10px rgba(243, 156, 18, 0.7);
  font-size: 1.7rem;
}

.safety-not-safe {
  color: #ff5a4a;
  font-weight: 900;
  text-shadow: 0 0 10px rgba(231, 76, 60, 0.7);
  font-size: 1.7rem;
}

.comparison-tabs {
  display: flex;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  margin-bottom: 2rem;
  position: sticky;
  top: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  z-index: 2;
  border-radius: 1rem 1rem 0 0;
}

.comparison-tab {
  flex: 1;
  text-align: center;
  padding: 1rem;
  cursor: pointer;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
  position: relative;
}

.comparison-tab.active {
  color: #f39c12;
}

.comparison-tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #f39c12;
}

/* Category badge styles */
.category-badge {
  font-size: 1.4rem;
  font-weight: 800;
  display: inline-block;
  padding: 0.6rem 2.5rem;
  border-radius: 2rem;
  margin: 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
  letter-spacing: 2px;
  text-align: center;
  min-width: 160px;
  text-transform: uppercase;
}

.category-harsh .category-badge {
  background-color: #e74c3c;
  color: white;
}

.category-moderate .category-badge {
  background-color: #f39c12;
  color: white;
}

.category-calm .category-badge {
  background-color: #2ecc71;
  color: white;
}

.beach-comparison-card {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 1rem;
  padding: 1rem 1.5rem;
  flex: 1;
  text-align: left;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 700px; /* Increased min-height to accommodate larger cards */
  max-width: 500px;
  margin: 0 auto;
}

.static-info {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0.75rem;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  text-align: center;
  font-size: 0.9rem;
}

.static-info p {
  margin: 0.3rem 0;
}

/* Styles for the Rip Identifier tab */
.ripIdentifier-tab {
  padding: 1rem;
}

.rip-upload-container {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  padding: 0.5rem; /* Reduced from 1rem */
  margin-top: 0.5rem;
}

.upload-area {
  border: 2px dashed rgba(255, 255, 255, 0.4);
  border-radius: 10px;
  min-height: 60px; /* Reduced from 80px */
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.2);
}

.upload-area:hover {
  border-color: rgba(255, 255, 255, 0.8);
  background: rgba(0, 0, 0, 0.3);
}

.upload-area.has-image {
  border-style: solid;
  border-color: rgba(255, 255, 255, 0.6);
}

.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0.5rem; /* Reduced from 1rem */
  color: rgba(255, 255, 255, 0.8);
}

.upload-icon {
  font-size: 1.5rem; /* Reduced from 2rem */
  margin-bottom: 0.25rem; /* Reduced from 0.5rem */
}

.upload-placeholder p {
  font-size: 0.9rem; /* Reduced from 1rem */
  font-weight: 500;
  margin: 0 0 0.5rem 0;
}

.upload-hint {
  font-size: 0.9rem;
  opacity: 0.7;
}

.hidden-file-input {
  display: none;
}

.uploaded-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  max-height: 350px;
}

.rip-actions {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem; /* Reduced from 1rem */
  justify-content: center;
}

.analyze-rip-button, .remove-image-button {
  padding: 0.6rem 1rem; /* Reduced from 0.8rem 1.5rem */
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  font-size: 0.9rem; /* Reduced from 1rem */
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 150px;
}

.analyze-rip-button {
  background: linear-gradient(135deg, #1a6aa5, #25a0c8);
  color: white;
  box-shadow: 0 4px 8px rgba(37, 160, 200, 0.3);
}

.analyze-rip-button:hover {
  background: linear-gradient(135deg, #155d91, #2196c1);
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(37, 160, 200, 0.4);
}

.analyze-rip-button:disabled {
  background: #95a5a6;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.remove-image-button {
  background: rgba(231, 76, 60, 0.2);
  color: #e74c3c;
  border: 1px solid #e74c3c;
}

.remove-image-button:hover {
  background: rgba(231, 76, 60, 0.3);
  transform: translateY(-2px);
}

.button-loader {
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s linear infinite;
}

.analyzing-message {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1.5rem 0;
  color: white;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.rip-analysis-result {
  background: rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  padding: 1.5rem;
  margin-top: 1.5rem;
}

.result-title {
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.3rem;
  text-align: center;
}

.result-image-container {
  position: relative;
  width: 100%;
  overflow: hidden;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.result-image {
  width: 100%;
  object-fit: contain;
  display: block;
  max-height: 300px;
}

.result-overlay {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0.5rem 1rem;
  border-bottom-left-radius: 8px;
}

.danger-badge {
  color: white;
  font-weight: 700;
  font-size: 1rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
}

.result-overlay.high {
  background: rgba(231, 76, 60, 0.8);
}

.result-overlay.medium {
  background: rgba(243, 156, 18, 0.8);
}

.result-overlay.low {
  background: rgba(46, 204, 113, 0.8);
}

.result-details {
  margin-top: 1rem;
}

.danger-indicator {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

.danger-level {
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.danger-indicator.high .danger-level {
  color: #e74c3c;
}

.danger-indicator.medium .danger-level {
  color: #f39c12;
}

.danger-indicator.low .danger-level {
  color: #2ecc71;
}

.danger-bar-container {
  height: 10px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  overflow: hidden;
}

.danger-bar {
  height: 100%;
  transition: width 0.8s ease;
}

.danger-indicator.high .danger-bar {
  background: #e74c3c;
}

.danger-indicator.medium .danger-bar {
  background: #f39c12;
}

.danger-indicator.low .danger-bar {
  background: #2ecc71;
}

.result-description {
  margin-bottom: 1rem;
  color: white;
  line-height: 1.5;
}

.safety-tips {
  background: rgba(0, 0, 0, 0.2);
  padding: 1rem;
  border-radius: 8px;
}

.safety-tips h5 {
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.safety-tips ul {
  margin: 0;
  padding-left: 1.5rem;
}

.safety-tips li {
  margin-bottom: 0.5rem;
  color: white;
}

.safety-tips li:last-child {
  margin-bottom: 0;
}

.rip-education {
  margin-top: 2rem;
  background: rgba(0, 0, 0, 0.2);
  padding: 1.5rem;
  border-radius: 10px;
}

.rip-education h4 {
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  text-align: center;
}

.rip-indicators {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.rip-indicator-item {
  flex: 1;
  min-width: 180px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.rip-indicator-item:hover {
  transform: translateY(-5px);
}

.indicator-image {
  width: 100%;
  height: 120px;
  object-fit: cover;
  display: block;
}

.rip-indicator-item p {
  padding: 0.8rem;
  margin: 0;
  text-align: center;
  font-size: 0.9rem;
  color: white;
}

@media (max-width: 768px) {
  .rip-indicators {
    flex-direction: column;
  }
  
  .rip-indicator-item {
    width: 100%;
  }
  
  .rip-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .analyze-rip-button, .remove-image-button {
    width: 100%;
  }
}

.side-panel {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
  padding: 20px;
  margin-top: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.side-panel h3 {
  color: #f39c12;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.5rem;
  text-align: center;
}

.side-panel p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.side-panel ul {
  list-style-type: none;
  padding-left: 1.5rem;
}

.side-panel li {
  margin-bottom: 0.75rem;
  color: white;
}

.side-panel li:before {
  content: "•";
  color: #f39c12;
  font-weight: bold;
  display: inline-block;
  width: 1rem;
  margin-left: -1rem;
}

/* Beach search suggestions popup overlay */
.search-suggestions-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
  pointer-events: none;
}

/* Beach search suggestions popup */
.search-suggestions-popup {
  position: absolute;
  background: rgba(0, 0, 0, 0.95);
  border-radius: 12px;
  padding: 1rem;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(243, 156, 18, 0.3);
  z-index: 10000;
  max-height: 350px;
  overflow-y: auto;
  backdrop-filter: blur(10px);
  animation: fadeIn 0.2s ease-out;
  pointer-events: auto;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.suggestions-popup-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.suggestion-popup-item {
  padding: 1rem 1.2rem;
  cursor: pointer;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  transition: all 0.2s ease;
  font-size: 1rem;
  border-radius: 8px;
  margin-bottom: 2px;
}

.suggestion-popup-item:hover {
  background: rgba(243, 156, 18, 0.2);
  padding-left: 1.5rem;
  transform: translateX(2px);
}

.suggestion-popup-item:active {
  background: rgba(243, 156, 18, 0.3);
  transform: scale(0.98);
}

.suggestion-popup-item:last-child {
  border-bottom: none;
}

.suggestion-popup-item:before {
  content: '🔍';
  margin-right: 0.8rem;
  opacity: 0.9;
  display: inline-block;
  transition: transform 0.2s ease;
}

.suggestion-popup-item:hover:before {
  transform: scale(1.2);
}

/* Beach report popup styles */
.beach-report-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(8px);
  z-index: 10000;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 10px;
  animation: fadeIn 0.3s ease-out;
}

/* Custom scrollbar for popups */
.report-content::-webkit-scrollbar {
  width: 10px;
}

.report-content::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.report-content::-webkit-scrollbar-thumb {
  background: rgba(243, 156, 18, 0.5);
  border-radius: 10px;
}

.report-content::-webkit-scrollbar-thumb:hover {
  background: rgba(243, 156, 18, 0.8);
}



.beach-report-popup {
  background: linear-gradient(135deg, rgba(15, 25, 40, 0.95), rgba(30, 40, 60, 0.95));
  border-radius: 16px;
  width: 95%;
  max-width: 1400px;
  height: 80vh;
  max-height: 80vh;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(243, 156, 18, 0.4);
  position: relative;
  animation: slideUp 0.4s ease-out;
  padding: 0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.popup-header {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9));
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  flex-shrink: 0;
}

.close-popup-btn {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.close-popup-btn:hover {
  background: rgba(231, 76, 60, 0.8);
  transform: rotate(90deg);
}

/* Success message after search */
.search-success-message {
  margin-top: 1rem;
  text-align: center;
}

.success-indicator {
  display: inline-flex;
  align-items: center;
  background: rgba(46, 204, 113, 0.15);
  border: 1px solid rgba(46, 204, 113, 0.5);
  color: #2ecc71;
  padding: 0.5rem 1rem;
  border-radius: 50px;
  gap: 0.5rem;
  animation: fadeIn 0.5s ease-out;
}

.success-icon {
  font-size: 1.2rem;
  font-weight: bold;
  background: rgba(46, 204, 113, 0.3);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.success-text {
  font-weight: 500;
  font-size: 0.95rem;
}

/* Compare success message and button */
.compare-success-message {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.view-comparison-btn {
  background: linear-gradient(135deg, #f39c12, #e67e22);
  color: white;
  border: none;
  padding: 0.6rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  margin-top: 0.5rem;
}

.view-comparison-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.rating-high {
  color: #e74c3c;
  border: 1px solid #e74c3c;
}

.rating-moderate {
  color: #f39c12;
  border: 1px solid #f39c12;
}

.rating-low {
  color: #2ecc71;
  border: 1px solid #2ecc71;
}

@keyframes glow {
  0% { text-shadow: 0 0 5px rgba(255, 255, 255, 0.3); }
  100% { text-shadow: 0 0 20px rgba(255, 255, 255, 0.7), 0 0 30px rgba(255, 255, 255, 0.5); }
}

/* === Overrides to ensure wave/current cards fill container === */
.condition-meaning {
  flex: 1;
  min-height: 0; /* allow child flex items to dictate height */
}

.wave-visual-card,
.current-visual-card {
  flex: 1;
  height: 100%;
  min-height: 120px;
}

.wave-image,
.current-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Add new styles for the redesigned compare info containers */
.compare-info-container {
  margin-bottom: 2rem;
  background: rgba(10, 20, 30, 0.25);
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

.compare-info-header {
  display: flex;
  align-items: center;
  padding: 0.8rem 1rem;
  background: rgba(0, 0, 0, 0.3);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.compare-info-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
}

.compare-info-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0;
}

.compare-info-content {
  display: flex;
  flex-direction: column;
}

.compare-info-image-container {
  position: relative;
  width: 100%;
  height: 180px; /* Increased from 160px to give more room */
  overflow: hidden;
  contain: strict; /* Improve layout stability */
}

.compare-info-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 40%; /* Position image to show more of the lower part */
  display: block;
  transition: transform 0.3s ease; /* Smooth transition for hover effects */
}

/* Add a subtle scale effect on hover, but keep it small to avoid overflow issues */
.compare-info-image-container:hover .compare-info-image {
  transform: scale(1.03);
}

.compare-info-hover-trigger {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
  transition: opacity 0.3s ease;
}

.compare-info-hover-prompt {
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  font-weight: 600;
  border: 2px solid rgba(243, 156, 18, 0.7);
}

.compare-info-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.compare-info-image-container:hover .compare-info-overlay {
  opacity: 1;
  visibility: visible;
}

.compare-info-image-container:hover .compare-info-hover-trigger {
  opacity: 0;
}

.compare-info-hover-details {
  width: 100%;
  text-align: center;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.75rem;
  background: rgba(0, 0, 0, 0.6);
  padding: 1rem;
  border-radius: 8px;
}

.compare-info-details {
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
}

.compare-info-details p {
  margin: 0.5rem 0;
  font-size: 1rem;
  line-height: 1.4;
}

.compare-info-highlight {
  color: #f39c12;
  font-weight: 700;
  font-size: 1.2rem;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
}

.suggestion-spacing {
  width: 100%;
  transition: all 0.4s ease-in-out;
  margin-top: 5px;
  overflow: hidden;
  position: relative;
  background: rgba(0, 0, 0, 0.15);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
  opacity: 0;
  padding: 8px 0;
}

.suggestion-indicator {
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  font-style: italic;
  padding: 5px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  margin: 5px auto;
  max-width: 80%;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.compare-wrapper {
  transition: all 0.3s ease-in-out;
  padding-bottom: 10px;
  min-height: 170px; /* Base height */
}

.compare-wrapper.expanded {
  margin-bottom: 20px;
  height: auto;
  min-height: 230px; /* Expanded height when suggestions are showing */
  background: rgba(0, 0, 0, 0.4);
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.compare-input-wrapper {
  transition: all 0.5s ease-in-out;
  position: relative;
  flex: 1;
  max-width: 48%;
  width: 100%;
}

/* This class is no longer used */

@media (max-width: 768px) {
  .suggestion-spacing {
    max-height: 230px !important;
  }
  
  .compare-input-wrapper.has-suggestions {
    margin-bottom: 20px;
  }
}

@media (max-width: 480px) {
  .suggestion-spacing {
    max-height: 250px !important;
  }
}

.compare-info-static {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0.75rem;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  text-align: center;
}

.compare-info-static p {
  margin: 0;
}

.compare-info-hover-details p {
  margin: 0;
  font-size: 1.2rem;
  line-height: 1.5;
  font-weight: 500;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
}

/* Media query adjustments for mobile */
@media (max-width: 768px) {
  .compare-info-container {
    margin-bottom: 1.5rem;
  }
  
  .compare-info-image-container {
    height: 180px;
  }
  
  .compare-info-hover-details p {
    font-size: 1rem;
  }
  
  .compare-info-highlight {
    font-size: 1.05rem;
  }
}
</style> 