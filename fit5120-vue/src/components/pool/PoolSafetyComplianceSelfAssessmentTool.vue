<template>
  <div class="flex flex-col items-center p-4 max-w-2xl mx-auto">
    <!-- Progress Bar -->
    <div class="w-full sticky top-0 bg-white z-10 py-2">
      <div class="text-center text-gray-600 text-sm mb-2">
        Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}
      </div>
      <div class="w-full h-2 bg-gray-200 rounded-full">
        <div
          class="h-2 bg-blue-500 rounded-full transition-all"
          :style="{ width: progress + '%' }"
        ></div>
      </div>
    </div>

    <!-- Question Card -->
    <transition name="fade" mode="out-in">
      <div key="question-{{ currentQuestionIndex }}" class="w-full mt-6">
        <h2 class="text-xl font-bold mb-4">{{ questions[currentQuestionIndex].question }}</h2>

        <div role="radiogroup" aria-label="Question Options" class="space-y-4">
          <label
            v-for="(option, idx) in questions[currentQuestionIndex].options"
            :key="idx"
            class="flex items-center gap-3 p-3 rounded-lg border cursor-pointer hover:bg-gray-100 transition"
          >
            <input
              type="radio"
              class="accent-blue-500 w-5 h-5"
              v-model="answers[currentQuestionIndex]"
              :value="option"
              @keydown.enter="nextQuestion"
              aria-label="Answer option"
            />
            <span>{{ option }}</span>
          </label>
        </div>

        <!-- Navigation Buttons -->
        <div class="flex justify-between mt-6">
          <button
            class="px-4 py-2 rounded bg-gray-300 hover:bg-gray-400 text-white disabled:opacity-50"
            @click="prevQuestion"
            :disabled="currentQuestionIndex === 0"
          >
            Back
          </button>

          <button
            v-if="!isLastQuestion"
            class="px-4 py-2 rounded bg-blue-500 hover:bg-blue-600 text-white disabled:opacity-50"
            @click="nextQuestion"
            :disabled="!answers[currentQuestionIndex]"
          >
            Next
          </button>

          <button
            v-else
            class="px-4 py-2 rounded bg-green-500 hover:bg-green-600 text-white"
            @click="showSummary = true"
            :disabled="!answers[currentQuestionIndex]"
          >
            Review Answers
          </button>
        </div>
      </div>
    </transition>

    <!-- Summary Page -->
    <transition name="fade" mode="out-in">
      <div v-if="showSummary" key="summary" class="w-full mt-6">
        <h2 class="text-xl font-bold mb-4">Review Your Answers</h2>
        <ul class="space-y-4">
          <li v-for="(question, index) in questions" :key="index">
            <div class="font-semibold">{{ question.question }}</div>
            <div class="ml-4">{{ answers[index] }}</div>
          </li>
        </ul>

        <div class="flex justify-between mt-6">
          <button
            class="px-4 py-2 rounded bg-gray-300 hover:bg-gray-400 text-white"
            @click="showSummary = false"
          >
            Edit Answers
          </button>

          <button
            class="px-4 py-2 rounded bg-green-500 hover:bg-green-600 text-white"
            @click="calculateScore"
          >
            Submit
          </button>
        </div>
      </div>
    </transition>

    <!-- Result Page -->
    <transition name="fade" mode="out-in">
      <div v-if="result" key="result" class="w-full mt-6 text-center">
        <h2 class="text-2xl font-bold mb-4">Your Pool Safety Status</h2>

        <div
          :class="badgeColor"
          class="inline-block px-6 py-3 rounded-full text-white font-bold text-lg mb-6"
        >
          {{ result }}
        </div>

        <h3 class="text-lg font-semibold mb-2">Recommended Action Steps:</h3>
        <ul class="list-disc list-inside text-left">
          <li v-for="(step, idx) in actionSteps" :key="idx">{{ step }}</li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';

const questions = [
  {
    question: 'Is your pool fully enclosed by a compliant safety barrier (fence)?',
    options: [
      'Yes, completely enclosed with no direct house access.',
      'Partially enclosed (e.g., open from the house side).',
      'No barrier or large gaps.',
    ],
  },
  {
    question: 'Does your pool gate automatically close and latch from any open position?',
    options: [
      'Yes, always self-closes and self-latches without effort.',
      'Sometimes needs a push or doesn’t latch properly.',
      'No, must be closed manually.',
    ],
  },
  {
    question: 'Is the gate latch mechanism located at least 1500mm above ground level?',
    options: ['Yes, latch is 1500mm or higher.', 'No, latch is lower than 1500mm.', 'Not sure.'],
  },
  {
    question: 'Are there any climbable objects within 900mm of the outside of the pool fence?',
    options: [
      'No, the area around the fence is clear.',
      'Some small objects are nearby but not climbable.',
      'Yes, climbable objects close to the fence.',
    ],
  },
  {
    question: 'Are there any gaps under or between the pool fence greater than 100mm?',
    options: ['No, all gaps are smaller than 100mm.', 'Some gaps might be larger than 100mm.', "I don't know / haven't checked."],
  },
  {
    question: 'Is constant active supervision provided by an adult whenever children are around the pool?',
    options: [
      'Yes, always supervised actively by an adult.',
      'Supervised sometimes but adults may get distracted.',
      'Often unsupervised or supervised by older children.',
    ],
  },
  {
    question: 'Are pool toys and inflatables removed immediately after swimming finishes?',
    options: [
      'Yes, always removed after swimming.',
      'Sometimes left in or near the pool.',
      'Usually left in the pool.',
    ],
  },
  {
    question: 'Can the entire surface of the pool be clearly seen from common supervising areas?',
    options: [
      'Yes, full clear view of entire pool.',
      'Some blind spots exist.',
      'No, major parts are not visible.',
    ],
  },
  {
    question: 'Are there any pet doors, windows, or unsecured doors from the house leading to the pool?',
    options: [
      'No, all accesses are securely fenced off or childproof.',
      'Some windows/doors could give direct access but usually locked.',
      'Yes, easy access from house to pool.',
    ],
  },
];

const currentQuestionIndex = ref(0);
const answers = ref(JSON.parse(localStorage.getItem('poolAnswers')) || Array(questions.length).fill(null));
const showSummary = ref(false);
const result = ref('');
const actionSteps = ref([]);

const progress = computed(() => ((currentQuestionIndex.value + 1) / questions.length) * 100);
const isLastQuestion = computed(() => currentQuestionIndex.value === questions.length - 1);

const nextQuestion = () => {
  if (currentQuestionIndex.value < questions.length - 1) {
    currentQuestionIndex.value++;
  }
};

const prevQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--;
  }
};

const calculateScore = () => {
  const highRiskAnswers = answers.value.filter((ans) =>
    ans && (ans.includes('No') || ans.includes('Not sure') || ans.includes('Usually'))
  ).length;

  if (highRiskAnswers === 0) {
    result.value = '🟢 Safe';
  } else if (highRiskAnswers <= 2) {
    result.value = '🟠 At Risk';
  } else {
    result.value = '🔴 Dangerous';
  }

  // Populate custom action steps
  actionSteps.value = [];
  answers.value.forEach((answer, idx) => {
    if (answer.includes('No') || answer.includes('Not sure') || answer.includes('Usually')) {
      actionSteps.value.push(`Review: ${questions[idx].question}`);
    }
  });

  localStorage.removeItem('poolAnswers'); // clear saved answers after submission
};

const badgeColor = computed(() => {
  if (result.value.includes('Safe')) return 'bg-green-500';
  if (result.value.includes('At Risk')) return 'bg-yellow-500 text-black';
  if (result.value.includes('Dangerous')) return 'bg-red-500';
  return '';
});

// Save progress to LocalStorage
watch(answers, (newAnswers) => {
  localStorage.setItem('poolAnswers', JSON.stringify(newAnswers));
}, { deep: true });

onMounted(() => {
  // Focus first option for accessibility
  setTimeout(() => {
    const firstInput = document.querySelector('input[type="radio"]');
    firstInput?.focus();
  }, 300);
});
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>









