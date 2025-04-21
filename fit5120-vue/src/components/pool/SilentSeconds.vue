<template>
  <div>
    <h2 class="text-2xl font-semibold mb-4">Silent Seconds: Understanding the Speed of Drowning</h2>
    <p class="mb-4">
      Drowning can happen in under 30 seconds — and often without a sound. Watch this real-life demonstration to understand the silent and sudden nature of pool-related accidents.
    </p>

    <div class="flex justify-center">
      <video class="w-full max-w-2xl" controls>
        <source :src="videoSource" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
</template>

<script>
import drowningVideo from '@/assets/drowning.mp4';

export default {
  name: 'SilentSeconds',
  data() {
    return {
      videoSource: drowningVideo
    }
  }
}
</script>

<style scoped>
.aspect-w-16 {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
}

.aspect-w-16 iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

  