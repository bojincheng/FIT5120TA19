<template>
  <div class="navbar-wrapper">
    <nav class="navbar">
      <div class="navbar-content">
        <!-- Logo on left -->
        <div class="navbar-logo">
          <router-link to="/" class="logo-link">
            <span class="logo-water">Water</span><span class="logo-wise">Wise</span><span class="logo-family">Family</span>
          </router-link>
        </div>
        
        <!-- Navigation tabs in middle -->
        <div class="navbar-tabs">
          <template v-for="tab in tabs" :key="tab.name">
            <router-link
              v-if="tab.path"
              :to="tab.path"
              class="navbar-tab"
              active-class="active"
            >
              <span class="tab-text">{{ tab.name }}</span>
            </router-link>
            <span
              v-else
              class="navbar-tab"
              style="cursor: default;"
            >
              <span class="tab-text">{{ tab.name }}</span>
            </span>
          </template>
        </div>
        
        <!-- Optional: Right side space -->
        <div class="navbar-right">
          <!-- Can be used for search, user menu, etc. -->
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'NavigationBar',
  data() {
    return {
      tabs: [
        { name: 'BEACH', path: '/beach' },
        { name: 'POOL', path: '/pool' },
        { name: 'RIVER', path: '/river' }
      ]
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap');

.navbar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

.navbar {
  background: rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
}

.navbar-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 1rem 2.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  flex: 1;
}

.logo-link {
  font-size: 1.6rem;
  text-decoration: none;
  letter-spacing: -0.5px;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.logo-water {
  font-weight: 600;
  color: #ffffff;
}

.logo-wise {
  font-weight: 700;
  color: #44ccff;
  text-shadow: 0 0 10px rgba(68, 204, 255, 0.5);
}

.logo-family {
  font-weight: 300;
  color: #ffffff;
  opacity: 0.9;
}

.logo-link:hover {
  text-shadow: 0 2px 8px rgba(255, 255, 255, 0.5);
}

.navbar-tabs {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex: 2;
}

.navbar-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.2rem;
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 400;
  transition: all 0.3s ease;
  font-size: 1.2rem;
  position: relative;
  letter-spacing: 0.5px;
}

.navbar-tab:hover {
  color: #ffffff;
}

.navbar-tab.active {
  color: #ffffff;
  font-weight: 500;
}

.navbar-tab::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: transparent;
  transition: all 0.3s ease;
}

.navbar-tab:hover::after {
  background-color: rgba(255, 255, 255, 0.5);
}

.navbar-tab.active::after {
  background-color: #ffffff;
  height: 2px;
}

.navbar-right {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar-content {
    padding: 0.8rem 1.5rem;
    flex-wrap: wrap;
  }
  
  .navbar-logo {
    flex: none;
    margin-right: 1rem;
  }
  
  .logo-link {
    font-size: 1.4rem;
    white-space: nowrap;
  }
  
  .navbar-tabs {
    flex: 3;
    justify-content: flex-end;
    gap: 1rem;
    flex-wrap: wrap;
  }
  
  .navbar-right {
    display: none;
  }

  .navbar-tab {
    white-space: nowrap;
    font-size: 1rem;
    padding: 0.4rem 0.1rem;
  }
}

@media (max-width: 600px) {
  .navbar-content {
    padding: 0.8rem 1rem;
    flex-direction: column;
    align-items: center;
  }
  
  .navbar-logo {
    margin-bottom: 0.5rem;
    text-align: center;
  }
  
  .navbar-tabs {
    justify-content: center;
    width: 100%;
  }
}

@media (max-width: 480px) {
  .navbar-content {
    padding: 0.8rem 1rem;
  }
  
  .logo-link {
    font-size: 1.2rem;
  }
  
  .navbar-tabs {
    gap: 0.6rem;
    justify-content: center;
    width: 100%;
  }
  
  .tab-text {
    display: block;
    font-size: 0.9rem;
  }
  
  .navbar-tab {
    padding: 0.3rem 0.1rem;
  }
}
</style> 