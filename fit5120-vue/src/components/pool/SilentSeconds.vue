<template>
  <div>
    <h2 class="text-2xl font-semibold mb-4">Silent Seconds: Understanding the Speed of Drowning</h2>
    <p class="mb-4">
      Drowning can happen in under 30 seconds — and often without a sound. Watch this real-life demonstration to understand the silent and sudden nature of pool-related accidents.
    </p>

    <div class="mb-4">
      <label for="language" class="block font-medium mb-1">Watch in your language:</label>
      <select v-model="selectedLanguage" id="language" class="p-2 border rounded w-full max-w-xs">
        <option value="English">English</option>
        <option value="Arabic">Arabic</option>
        <option value="Mandarin">Mandarin</option>
        <option value="Cantonese">Cantonese</option>
        <option value="Cambodian">Cambodian</option>
        <option value="Macedonian">Macedonian</option>
        <option value="Somali">Somali</option>
        <option value="Turkish">Turkish</option>
        <option value="Vietnamese">Vietnamese</option>
      </select>
    </div>

    <div class="video-container">
      <video
        :key="selectedLanguage"
        class="video-player"
        controls
        preload="metadata"
      >
        <source :src="videoPath" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SilentSeconds',
  data() {
    return {
      selectedLanguage: 'English'
    };
  },
  computed: {
    videoPath() {
      return `/videos/Drowning_${this.selectedLanguage}.mp4`;
    }
  }
};
</script>

<style scoped>
.video-container {
  display: flex;
  justify-content: center;
}

.video-player {
  width: 100%;
  max-width: 720px; /* Matches typical HD video width */
  height: auto;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style>
