<template>
  <div class="pool-nav-container">
    <!-- Top Navigation Bar -->
    <nav class="top-nav">
      <router-link to="/home" class="nav-brand" @click="scrollToTop">WaterWiseFamily</router-link>
      
      <div class="nav-links">
        <router-link to="/pool-safety" class="nav-link" :class="{ active: isActive('/pool-safety') }">Pool Safety Basics</router-link>
        
        <!-- Supervision dropdown -->
        <div class="nav-dropdown" @mouseenter="supervisionDropdownOpen = true" @mouseleave="delayedCloseSupervisionDropdown" @click="keepSupervisionDropdownOpen">
          <router-link to="/pool-supervision" class="nav-link dropdown-trigger" :class="{ active: isActiveSupervision() }">
            Supervision Guidelines
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </router-link>
          
          <div class="dropdown-menu" v-show="supervisionDropdownOpen" @click.stop>
            <router-link to="/pool-supervision" class="dropdown-item" :class="{ active: isActive('/pool-supervision') }">
              Understanding Danger
            </router-link>
            <router-link to="/backyard-pool" class="dropdown-item" :class="{ active: isActive('/backyard-pool') }">
              Backyard Pool Safety
            </router-link>
            <div @click="showQuizModal" class="dropdown-item">
              Test Your Readiness
            </div>
          </div>
        </div>
        
      </div>
      
      <div class="safety-mode-selector">
        <div class="selected-mode" @click="toggleModeDropdown">
          <span>{{ safetyMode }}</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
        <div class="mode-dropdown" v-show="modeDropdownOpen">
          <div class="mode-option" @click="selectMode('Beach Safety')" :class="{ active: safetyMode === 'Beach Safety' }">Beach Safety</div>
          <div class="mode-option" @click="selectMode('Pool Safety')" :class="{ active: safetyMode === 'Pool Safety' }">Pool Safety</div>
        </div>
      </div>
    </nav>
    
    <!-- Mobile Menu Toggle Button -->
    <div class="mobile-toggle" @click="toggleMenu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
    </div>
    
    <!-- Mobile Menu Overlay -->
    <div class="mobile-overlay" v-if="menuOpen" @click="toggleMenu"></div>
    
    <!-- Mobile Menu -->
    <div class="mobile-menu" :class="{ 'open': menuOpen }">
      <div class="mobile-menu-header">
        <router-link to="/home" class="brand-logo" @click="scrollToTop">WaterWiseFamily</router-link>
        <div class="close-menu" @click="toggleMenu">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </div>
      </div>
      
      <div class="mobile-mode-selector">
        <div class="mobile-mode-label">Safety Mode:</div>
        <div class="mobile-mode-options">
          <div class="mobile-mode-option" 
               @click="selectMode('Beach Safety')" 
               :class="{ active: safetyMode === 'Beach Safety' }">
            Beach Safety
          </div>
          <div class="mobile-mode-option" 
               @click="selectMode('Pool Safety')" 
               :class="{ active: safetyMode === 'Pool Safety' }">
            Pool Safety
          </div>
        </div>
      </div>
      
      <div class="mobile-nav-links">
        <router-link to="/pool-safety" class="mobile-nav-link" :class="{ active: isActive('/pool-safety') }">Pool Safety Basics</router-link>
        
        <!-- Mobile Supervision dropdown -->
        <div class="mobile-dropdown">
          <div class="mobile-dropdown-header" @click="toggleMobileSupervisionDropdown">
            <router-link to="/pool-supervision" class="mobile-nav-link" :class="{ active: isActiveSupervision() }">Supervision Guidelines</router-link>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="{ 'rotated': mobileSupervisionDropdownOpen }"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
          <div class="mobile-dropdown-content" v-show="mobileSupervisionDropdownOpen">
            <router-link to="/pool-supervision" class="mobile-dropdown-item" :class="{ active: isActive('/pool-supervision') }">
              Understanding Danger
            </router-link>
            <router-link to="/backyard-pool" class="mobile-dropdown-item" :class="{ active: isActive('/backyard-pool') }">
              Backyard Pool Safety
            </router-link>
            <div @click="showQuizModal" class="mobile-dropdown-item">
              Test Your Readiness
            </div>
          </div>
        </div>
      </div>
      
      <div class="mobile-safety-tip">
        <div class="tip-icon">💡</div>
        <div class="tip-text">Always maintain active supervision - never leave children unattended near a pool.</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PoolMenu',
  props: {
    menuOpen: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      modeDropdownOpen: false,
      supervisionDropdownOpen: false,
      mobileSupervisionDropdownOpen: false,
      safetyMode: 'Pool Safety',
      closeTimeout: null,
      dropdownClicked: false,
      supervisionDropdownCloseTimer: null,
      quizModalOpen: false
    }
  },
  mounted() {
    // Close dropdown when clicking outside
    document.addEventListener('click', this.closeDropdownOutside);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.closeDropdownOutside);
    
    // Clear any pending timeouts to prevent memory leaks
    if (this.closeTimeout) {
      clearTimeout(this.closeTimeout);
    }
  },
  methods: {
    toggleMenu() {
      this.$emit('toggle-menu');
    },
    toggleModeDropdown(event) {
      // Stop propagation to prevent document click handler from immediately closing it
      event.stopPropagation();
      this.modeDropdownOpen = !this.modeDropdownOpen;
      this.supervisionDropdownOpen = false;
    },
    toggleSupervisionDropdown(event) {
      // Keep this method for mobile support, but for desktop we're using hover
      event.stopPropagation();
      this.supervisionDropdownOpen = !this.supervisionDropdownOpen;
      this.modeDropdownOpen = false;
    },
    toggleMobileSupervisionDropdown() {
      this.mobileSupervisionDropdownOpen = !this.mobileSupervisionDropdownOpen;
    },
    selectMode(mode) {
      this.safetyMode = mode;
      this.modeDropdownOpen = false;
      
      // Navigate to the appropriate page based on the selected mode
      if (mode === 'Beach Safety') {
        this.$router.push('/beach-safety');
      } else if (mode === 'Pool Safety') {
        this.$router.push('/pool-safety');
      }
      
      // Emit event for parent component to handle mode change
      this.$emit('mode-change', mode);
    },
    closeDropdownOutside(event) {
      // Handle safety mode dropdown
      const modeSelector = document.querySelector('.safety-mode-selector');
      if (modeSelector && !modeSelector.contains(event.target)) {
        this.modeDropdownOpen = false;
      }
      
      // We don't need this for supervision dropdown anymore since it's hover-based
      // but keep it for mobile support
    },
    isActive(route) {
      // Exact path matching for all routes
      return this.$route.path === route;
    },
    isActiveSupervision() {
      // Check if the current route is either pool-supervision or backyard-pool
      return this.$route.path === '/pool-supervision' || this.$route.path === '/backyard-pool' || this.$route.path === '/pool-safety-quiz';
    },
    showQuizModal() {
      // Emit event to show quiz modal
      this.$emit('show-quiz');
      
      // Close mobile menu if open
      if (this.menuOpen) {
        this.toggleMenu();
      }
      
      // Close dropdowns
      this.supervisionDropdownOpen = false;
      this.mobileSupervisionDropdownOpen = false;
    },
    delayedCloseSupervisionDropdown() {
      // Clear any existing timeout to prevent multiple timeouts
      if (this.closeTimeout) {
        clearTimeout(this.closeTimeout);
      }
      
      // If the dropdown was clicked, don't close it on mouseleave
      if (this.dropdownClicked) {
        return;
      }
      
      // Set a timeout to close the dropdown after a delay
      this.closeTimeout = setTimeout(() => {
        this.supervisionDropdownOpen = false;
      }, 500); // 500ms delay before closing
    },
    keepSupervisionDropdownOpen() {
      // Mark the dropdown as clicked to prevent it from closing on mouseleave
      this.dropdownClicked = true;
      
      // Add a one-time click handler to the document to close the dropdown when clicking elsewhere
      document.addEventListener('click', this.closeSupervisionDropdown, { once: true });
    },
    closeSupervisionDropdown() {
      this.supervisionDropdownOpen = false;
      this.dropdownClicked = false;
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    }
  }
}
</script>

<style scoped>
/* Top Navigation Bar Styles */
.pool-nav-container {
  position: relative;
  width: 100%;
  z-index: 15;
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 2rem;
  background: rgba(0, 61, 91, 0.9);
  backdrop-filter: blur(10px);
  box-shadow: 0 3px 15px rgba(0, 0, 0, 0.3);
  border-bottom: 2px solid rgba(0, 225, 255, 0.4);
}

.nav-brand {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  text-decoration: none;
  transition: all 0.2s ease;
}

.nav-brand:hover {
  color: #00e1ff;
  transform: translateY(-1px);
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.5rem 0;
  position: relative;
  transition: all 0.2s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #00e1ff;
  transition: width 0.2s ease;
}

.nav-link:hover {
  color: #ffffff;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link.active {
  color: #00e1ff;
}

.nav-link.active::after {
  width: 100%;
  background: #00e1ff;
}

.safety-mode-selector {
  position: relative;
}

.selected-mode {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0, 149, 168, 0.5);
  padding: 0.4rem 1rem;
  border-radius: 2rem;
  border: 1px solid rgba(0, 225, 255, 0.6);
  cursor: pointer;
  transition: all 0.2s ease;
}

.selected-mode:hover {
  background: rgba(0, 149, 168, 0.7);
  transform: translateY(-2px);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
}

.selected-mode span {
  font-weight: 700;
  font-size: 0.95rem;
  color: white;
}

.selected-mode svg {
  color: white;
  transition: transform 0.3s ease;
}

.selected-mode:hover svg {
  transform: translateY(2px);
}

.mode-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: rgba(0, 61, 91, 0.95);
  border-radius: 0.75rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
  padding: 0.5rem;
  z-index: 10;
  min-width: 160px;
  border: 1px solid rgba(0, 225, 255, 0.4);
  animation: fadeDown 0.2s ease-out;
}

@keyframes fadeDown {
  from { 
    opacity: 0;
    transform: translateY(-10px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

.mode-option {
  padding: 0.75rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.85);
  border-radius: 0.5rem;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.mode-option:before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: transparent;
  margin-right: 8px;
  border: 1px solid rgba(0, 196, 217, 0.5);
  transition: all 0.2s ease;
}

.mode-option:hover {
  background: rgba(0, 196, 217, 0.2);
  color: white;
}

.mode-option.active {
  background: rgba(0, 196, 217, 0.3);
  color: white;
}

.mode-option.active:before {
  background: #00e1ff;
  box-shadow: 0 0 5px rgba(0, 196, 217, 0.5);
}

/* Mobile Menu Styles */
.mobile-toggle {
  display: none;
  position: absolute;
  right: 1.5rem;
  top: 1.2rem;
  align-items: center;
  justify-content: center;
  color: white;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 15;
}

.mobile-toggle:hover {
  background: rgba(255, 255, 255, 0.3);
}

.mobile-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 48;
  backdrop-filter: blur(3px);
  transition: all 0.3s ease;
}

.mobile-menu {
  position: fixed;
  top: 0;
  right: -300px;
  width: 280px;
  height: 100%;
  background: linear-gradient(165deg, #00526e, #003045);
  z-index: 49;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  transition: right 0.3s ease;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.mobile-menu.open {
  right: 0;
}

.mobile-menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.brand-logo {
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  text-decoration: none;
  transition: all 0.2s ease;
}

.brand-logo:hover {
  color: #00e1ff;
}

.close-menu {
  cursor: pointer;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.close-menu:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: rotate(90deg);
}

.mobile-mode-selector {
  margin: 0.5rem 1.5rem 1rem;
  padding: 1rem;
  border-radius: 0.75rem;
  background: rgba(0, 196, 217, 0.15);
  border: 1px solid rgba(0, 196, 217, 0.3);
}

.mobile-mode-label {
  font-weight: 600;
  color: white;
  margin-bottom: 0.5rem;
}

.mobile-mode-options {
  display: flex;
  gap: 0.5rem;
  background: rgba(0, 137, 179, 0.5);
  padding: 0.25rem;
  border-radius: 0.5rem;
}

.mobile-mode-option {
  flex: 1;
  padding: 0.6rem 1rem;
  border-radius: 0.35rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}

.mobile-mode-option:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.mobile-mode-option.active {
  background: rgba(0, 196, 217, 0.35);
  color: white;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  padding: 1rem 0;
}

.mobile-nav-link {
  display: block;
  padding: 1rem 1.5rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  border-left: 3px solid transparent;
  font-weight: 500;
  transition: all 0.2s ease;
}

.mobile-nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-left-color: #00e1ff;
}

.mobile-nav-link.active {
  background: rgba(0, 196, 217, 0.15);
  color: #00e1ff;
  border-left-color: #00e1ff;
}

.mobile-safety-tip {
  margin-top: auto;
  padding: 1rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  gap: 0.8rem;
  align-items: flex-start;
}

.tip-icon {
  font-size: 1.5rem;
}

.tip-text {
  font-size: 0.9rem;
  line-height: 1.4;
  color: rgba(255, 255, 255, 0.9);
}

/* Dropdown Menu Styles */
.nav-dropdown {
  position: relative;
}

.dropdown-trigger {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
}

.dropdown-trigger svg {
  transition: transform 0.3s ease;
}

.dropdown-trigger:hover svg {
  transform: translateY(2px);
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 10px);
  left: 0;
  min-width: 220px;
  background: rgba(0, 61, 91, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 0.75rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
  padding: 0.5rem;
  z-index: 10;
  border: 1px solid rgba(0, 225, 255, 0.3);
  animation: fadeDown 0.2s ease-out;
  /* Adding a small amount of space before the dropdown to prevent it from closing too quickly */
  margin-top: 10px;
  /* Adding a longer transition time for closing */
  transition: opacity 0.3s ease, visibility 0.3s ease;
  /* These properties ensure smooth transition when showing/hiding the dropdown */
  opacity: 1;
}

.dropdown-menu::before {
  content: '';
  position: absolute;
  top: -20px; /* Increased from -10px to create a larger buffer zone */
  left: 0;
  width: 100%;
  height: 20px; /* Increased from 10px */
  background: transparent;
}

/* New styles to create a buffer area around the dropdown */
.nav-dropdown:hover .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transition-delay: 0.1s; /* Add a small delay before showing */
}

.dropdown-menu::after {
  content: '';
  position: absolute;
  top: 100%;
  left: -20px;
  width: calc(100% + 40px); /* Extend 20px on each side */
  height: 30px;
  background: transparent;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.75rem 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.85);
  border-radius: 0.5rem;
  font-weight: 500;
  text-decoration: none;
}

.dropdown-item:hover {
  background: rgba(0, 196, 217, 0.2);
  color: white;
}

.dropdown-item.active {
  background: rgba(0, 196, 217, 0.3);
  color: white;
}

.step-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  font-size: 0.8rem;
  border-radius: 50%;
  background: rgba(0, 225, 255, 0.3);
  color: white;
  font-weight: 700;
}

.dropdown-item.active .step-number {
  background: #00e1ff;
}

/* Mobile Dropdown Styles */
.mobile-dropdown {
  width: 100%;
}

.mobile-dropdown-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  cursor: pointer;
}

.mobile-dropdown-header svg {
  margin-right: 1.5rem;
  transition: transform 0.3s ease;
}

.mobile-dropdown-header svg.rotated {
  transform: rotate(180deg);
}

.mobile-dropdown-content {
  padding: 0.5rem 0;
  background: rgba(0, 41, 61, 0.5);
}

.mobile-dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1.5rem 0.8rem 2.5rem;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.2s ease;
  font-size: 0.95rem;
}

.mobile-dropdown-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.mobile-dropdown-item.active {
  background: rgba(0, 196, 217, 0.15);
  color: #00e1ff;
}

.mobile-step-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  font-size: 0.8rem;
  border-radius: 50%;
  background: rgba(0, 225, 255, 0.2);
  color: white;
  font-weight: 700;
}

.mobile-dropdown-item.active .mobile-step-number {
  background: rgba(0, 225, 255, 0.5);
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link {
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
  .top-nav {
    padding: 1rem;
  }
  
  .nav-brand {
    margin: 0 auto;
  }
  
  .nav-links, .safety-mode-selector {
    display: none;
  }
  
  .mobile-toggle {
    display: flex;
  }
}

@media (max-width: 480px) {
  .mobile-menu {
    width: 250px;
  }
  
  .mobile-nav-link {
    padding: 0.8rem 1.25rem;
  }
}
</style> 