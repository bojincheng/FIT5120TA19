<template>
  <div v-if="show" class="popup-overlay" @click.self="closePopup">
    <div class="popup-container">
      <div class="popup-header">
        <h3>{{ getStateFullName(selectedState) }} Pool Fencing Requirements</h3>
        <button @click="closePopup" class="close-button" aria-label="Close">&times;</button>
      </div>
      <div class="popup-content">
        <div class="regulation-details">
          <div class="regulation-item">
            <h6><span class="requirement-icon">📏</span> Barrier Requirements</h6>
            <ul>
              <li v-for="req in barrierRequirements" :key="req">{{ req }}</li>
            </ul>
          </div>
          <div class="regulation-item">
            <h6><span class="requirement-icon">📜</span> Legal Requirements</h6>
            <ul>
              <li v-for="req in legalRequirements" :key="req">{{ req }}</li>
            </ul>
          </div>
        </div>
        <div class="regulation-link">
          <a :href="officialLink" target="_blank" class="resource-link">
            <span class="link-icon">🔗</span> Official {{ selectedState.toUpperCase() }} Swimming Pool Safety Guidelines
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegulationPopup',
  props: {
    show: {
      type: Boolean,
      required: true,
    },
    selectedState: {
      type: String,
      required: true,
    },
    australianStates: {
      type: Array,
      required: true,
    }
  },
  computed: {
    barrierRequirements() {
      const requirements = {
        nsw: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
        vic: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Self-closing and self-latching gates that open outward',
          'Different requirements based on pool construction date',
        ],
        qld: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
        wa: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Self-closing and self-latching gates that open outward',
          'Specific regulations for isolation fencing vs boundary fencing',
        ],
        sa: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
        tas: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
        nt: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
        act: [
          'Minimum fence height: 1.2 meters',
          'Maximum gap from ground: 100mm',
          'No climbable objects within 900mm of fence',
          'Gates must open outwards, away from pool area',
          'Gates must be self-closing and self-latching',
        ],
      };
      return requirements[this.selectedState] || [];
    },
    legalRequirements() {
      const requirements = {
        nsw: [
          'All pools must be registered on the NSW Swimming Pool Register',
          'Mandatory pool barrier certification required when selling or leasing property',
          'Compliance certificate valid for 3 years',
          'Penalties of up to $5,500 for non-compliance',
        ],
        vic: [
          'All pools and spas must be registered with local council',
          'Mandatory safety barrier inspections every 4 years',
          'Certificate of compliance required',
          'Penalties over $1,652 for individuals and $8,261 for companies',
        ],
        qld: [
          'Pool safety certificate required when selling or leasing property',
          'Pool safety certificates valid for 2 years for shared pools and 1 year for non-shared pools',
          'All pools must be registered in the state pool register',
          'Penalties of up to $21,000 for non-compliance',
        ],
        wa: [
          'Mandatory inspections at least once every 4 years',
          'Local government authorities responsible for compliance inspections',
          'Pool owners must ensure barriers are maintained',
          'Penalties up to $5,000 for non-compliance',
        ],
        sa: [
          'Safety barriers required for all pools and spas deeper than 30cm',
          'Development approval required before installing a pool',
          'Pool must be inspected within 2 months after construction',
          'Penalties for non-compliance with swimming pool laws',
        ],
        tas: [
          'All pools must have compliant barriers',
          'Compliance required for pools capable of holding water to a depth of 30cm or more',
          'Certificate of compliance required for new pools',
          'Heavy penalties for non-compliance with pool safety laws',
        ],
        nt: [
          'All pools must have compliant barriers',
          'Pool safety compliance required when selling a property',
          'Regular maintenance of pool barriers required',
          'Significant penalties for non-compliance',
        ],
        act: [
          'Pool barriers must comply with Australian Standard AS1926.1',
          'Building approval required before installing a pool',
          'Development approval may be required from the Planning Authority',
          'Penalties apply for non-compliant barriers',
        ],
      };
      return requirements[this.selectedState] || [];
    },
    officialLink() {
      const linkMap = {
        nsw: 'https://www.fairtrading.nsw.gov.au/housing-and-property/pool-safety',
        vic: 'https://www.vba.vic.gov.au/consumers/swimming-pools',
        qld: 'https://www.qbcc.qld.gov.au/home-building-owners/pool-safety',
        wa: 'https://www.commerce.wa.gov.au/building-and-energy/swimming-pool-and-spa-pool-safety',
        sa: 'https://www.sa.gov.au/topics/housing/safety-and-modifications/pool-safety',
        tas: 'https://www.cbos.tas.gov.au/topics/housing/building-or-renovating/swimming-pool-safety',
        nt: 'https://nt.gov.au/property/building/build-or-renovate-a-home/swimming-pool-safety',
        act: 'https://www.accesscanberra.act.gov.au/s/article/building-approval-and-requirements-tab-swimming-pools',
      };
      return linkMap[this.selectedState] || '#';
    }
  },
  methods: {
    closePopup() {
      this.$emit('close');
    },
    getStateFullName(stateCode) {
      const state = this.australianStates.find(s => s.code === stateCode);
      return state ? state.name : stateCode.toUpperCase();
    }
  }
};
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000; /* High z-index to ensure it's on top */
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  animation: overlayFadeIn 0.3s ease-out;
}

@keyframes overlayFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.popup-container {
  background: rgba(10, 25, 41, 0.95); /* Dark blue, slightly transparent */
  color: #e0f7fa; /* Light cyan text */
  border-radius: 16px;
  padding: 0; /* Padding will be handled by header/content */
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(77, 182, 243, 0.3); /* Main shadow + subtle blue glow */
  width: 90%;
  max-width: 800px; /* Increased from 700px */
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  overflow: hidden; /* Important for managing scrolling content */
  border: 1px solid rgba(77, 182, 243, 0.2); /* Subtle border */
  animation: popupSlideIn 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
  transform: scale(0.95);
  opacity: 0;
}

@keyframes popupSlideIn {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.popup-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 1.5rem;
  background: linear-gradient(135deg, rgba(1, 79, 134, 0.9), rgba(7, 56, 104, 0.95)); /* Darker blue gradient */
  border-bottom: 1px solid rgba(77, 182, 243, 0.4); /* Accent border */
  color: #ffffff;
  text-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

.popup-header h3 {
  margin: 0;
  font-size: 1.8rem; /* Increased from 1.6rem */
  font-weight: 700;
  letter-spacing: 0.02em;
}

.close-button {
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.2);
  color: #e0f7fa;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 1.8rem;
  line-height: 1;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 2px; /* Optical adjustment for &times; */
}

.close-button:hover {
  background: rgba(239, 83, 80, 0.8); /* Red hover for close */
  color: white;
  transform: rotate(90deg) scale(1.1);
  border-color: rgba(239, 83, 80, 1);
}

.popup-content {
  padding: 1.5rem;
  overflow-y: auto; /* Enable scrolling for content */
  flex-grow: 1;
  background-color: rgba(10, 35, 61, 0.8); /* Slightly lighter than container for depth */
}

/* Scrollbar styling for webkit browsers */
.popup-content::-webkit-scrollbar {
  width: 8px;
}

.popup-content::-webkit-scrollbar-track {
  background: rgba(0,0,0,0.1);
  border-radius: 4px;
}

.popup-content::-webkit-scrollbar-thumb {
  background: rgba(77, 182, 243, 0.6);
  border-radius: 4px;
}

.popup-content::-webkit-scrollbar-thumb:hover {
  background: rgba(77, 182, 243, 0.8);
}


.regulation-details {
  display: grid;
  grid-template-columns: 1fr; /* Single column for popup */
  gap: 1.5rem; /* Spacing between barrier and legal sections */
  margin-bottom: 1.5rem;
}

.regulation-item {
  background: rgba(20, 50, 80, 0.6); /* Darker item background */
  border-radius: 12px;
  padding: 1.2rem;
  border: 1px solid rgba(77, 182, 243, 0.2);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.regulation-item h6 {
  color: #82d8ff; /* Lighter blue for headings */
  font-size: 1.6rem; /* Increased from 1.4rem */
  margin: 0 0 0.8rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(77, 182, 243, 0.3);
  padding-bottom: 0.6rem;
  letter-spacing: 0.01em;
}

.requirement-icon {
  margin-right: 0.8rem;
  font-size: 1.8rem; /* Increased from 1.6rem */
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.2));
}

.regulation-item ul {
  margin: 0;
  padding-left: 1.5rem;
  color: #c5e8ef; /* Slightly dimmer text for list items */
  list-style: none;
}

.regulation-item li {
  margin-bottom: 0.6rem;
  line-height: 1.5;
  position: relative;
  font-size: 1.2rem; /* Increased from 1.05rem */
}

.regulation-item li::before {
  content: '◈'; /* Diamond bullet */
  position: absolute;
  left: -1.5rem;
  top: 0.1em;
  color: #82d8ff;
  font-size: 1.15rem; /* Increased from 1.05rem */
  background: rgba(20, 60, 100, 0.7);
  font-weight: 600;
}


.regulation-link {
  padding-top: 1.5rem;
  text-align: center;
  border-top: 1px solid rgba(77, 182, 243, 0.3);
}

.resource-link {
  display: inline-flex;
  align-items: center;
  color: #82d8ff;
  text-decoration: none;
  padding: 0.7rem 1.5rem;
  border: 1px solid rgba(77, 182, 243, 0.5);
  border-radius: 30px; /* Pill shape */
  transition: all 0.3s ease;
  background: rgba(20, 60, 100, 0.7);
  font-weight: 600;
  font-size: 1.05rem; /* Increased from 0.95rem */
}

.resource-link:hover {
  background: rgba(77, 182, 243, 0.3);
  border-color: rgba(120, 200, 255, 0.8);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.link-icon {
  margin-right: 0.7rem;
  font-size: 1.4rem; /* Increased from 1.3rem */
}

@media (max-width: 768px) {
  .popup-container {
    width: 95%;
    max-height: 85vh;
  }
  .popup-header h3 {
    font-size: 1.2rem;
  }
  .popup-content {
    padding: 1.2rem;
  }
  .regulation-item h6 {
    font-size: 1.1rem;
  }
  .regulation-item li {
    font-size: 0.9rem;
  }
  .resource-link {
    font-size: 0.9rem;
    padding: 0.6rem 1.2rem;
  }
}

@media (max-width: 480px) {
  .popup-header {
    padding: 1rem;
  }
  .popup-header h3 {
    font-size: 1.1rem;
  }
  .close-button {
    width: 32px;
    height: 32px;
    font-size: 1.6rem;
  }
  .popup-content {
    padding: 1rem;
  }
   .regulation-item {
    padding: 1rem;
  }
  .regulation-item h6 {
    font-size: 1rem;
  }
  .regulation-item li {
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
  }
   .resource-link {
    font-size: 0.85rem;
    padding: 0.5rem 1rem;
  }
}
</style> 