<template>
  <div class="landing-container">
    <div class="video-background">
      <video autoplay loop muted playsinline>
        <source src="/videos/landing_background.mp4" type="video/mp4">
      </video>
      <div class="overlay"></div>
    </div>
    <div class="content">
      <div class="static-text">
        <h1 class="title-animation">Introducing <span class="highlight">Water Wise Family</span></h1>
        <p class="subtitle-animation">Protect your child from becoming a victim of drowning — a few moments of learning can mean a lifetime of safety.</p>
      </div>
      <div class="buttons-container">
        <div class="button-wrapper first-time-wrapper">
          <button class="main-button first-time-button" @click="navigateToExperience">
            Start Your Journey
            <span class="arrow">→</span>
          </button>
          <div class="button-description">
            <span class="headphones-icon">🎧</span> For first-time users (headphones recommended)
          </div>
        </div>
        
        <div class="button-wrapper">
          <button class="secondary-button returning-button" @click="navigateToHome">
            Go to Home Page
            <span class="arrow">→</span>
          </button>
          <div class="button-description">
            For returning users
          </div>
        </div>
      </div>
    </div>
    <div class="decoration left-decoration"></div>
    <div class="decoration right-decoration"></div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  methods: {
    navigateToExperience() {
      // For new users, navigate to the loading page for the full experience
      this.$router.push('/loading');
    },
    navigateToHome() {
      // For returning users, go directly to home
      this.$router.push('/home');
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

.landing-container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  padding: 2rem;
  overflow: hidden;
  position: relative;
}

.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
}

.video-background video {
  position: absolute;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  object-fit: cover;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.65) 100%);
  z-index: 1;
}

.content {
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4rem;
  z-index: 2;
  position: relative;
  animation: fadeIn 1s ease forwards;
}

.static-text {
  text-align: center;
  max-width: 90%;
}

.title-animation {
  animation: fadeInUp 1s ease-out forwards;
  opacity: 0;
}

.subtitle-animation {
  animation: fadeInUp 1s ease-out 0.3s forwards;
  opacity: 0;
}

.static-text h1 {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: 0.02em;
  color: #ffffff;
  margin: 0 0 1.5rem 0;
  position: relative;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.highlight {
  color: #4ecdc4;
  position: relative;
}

.highlight::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #4ecdc4;
  transform: scaleX(0);
  transform-origin: left;
  animation: expandLine 1.2s ease-out 1.2s forwards;
}

.static-text p {
  font-size: clamp(1.2rem, 2.5vw, 1.7rem);
  font-weight: 300;
  line-height: 1.7;
  color: #ffffff;
  opacity: 0.9;
  max-width: 800px;
  margin: 0 auto;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.buttons-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
  margin-top: 1rem;
  animation: fadeIn 1.5s ease-out 0.8s forwards;
  opacity: 0;
  width: 100%;
  max-width: 350px;
}

.button-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.6rem;
  width: 100%;
}

.button-description {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.85);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.headphones-icon {
  font-size: 1.1rem;
}

.main-button, .secondary-button {
  font-family: 'Montserrat', sans-serif;
  padding: 1.1rem 2rem;
  font-size: clamp(1.1rem, 2vw, 1.3rem);
  font-weight: 600;
  border-radius: 50px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.7rem;
  transition: all 0.3s ease;
  letter-spacing: 0.05em;
  position: relative;
  overflow: hidden;
  width: 100%;
  box-sizing: border-box;
}

.main-button {
  background: linear-gradient(45deg, #ff3333, #ff6666);
  color: white;
  border: none;
  box-shadow: 0 8px 25px rgba(255, 68, 68, 0.4);
}

.main-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(255, 68, 68, 0.6);
  background: linear-gradient(45deg, #ff4444, #ff7777);
}

.secondary-button {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.7);
  box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15);
}

.secondary-button:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.2);
  border-color: white;
  box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2);
}

.arrow {
  font-size: 1.2em;
  transition: transform 0.3s ease;
}

.main-button:hover .arrow, .secondary-button:hover .arrow {
  transform: translateX(5px);
}

.decoration {
  position: absolute;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
  border-radius: 50%;
  z-index: 1;
}

.left-decoration {
  top: 10%;
  left: 5%;
  animation: float 8s ease-in-out infinite;
}

.right-decoration {
  bottom: 10%;
  right: 5%;
  animation: float 8s ease-in-out infinite reverse;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes expandLine {
  to { transform: scaleX(1); }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

@media (max-width: 768px) {
  .landing-container {
    padding: 1rem;
  }
  
  .content {
    gap: 3rem;
  }
  
  .static-text h1 {
    margin-bottom: 1rem;
  }
  
  .buttons-container {
    gap: 1.5rem;
  }
}
</style> 