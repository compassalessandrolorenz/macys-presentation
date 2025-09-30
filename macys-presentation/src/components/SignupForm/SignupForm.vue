<template>
  <div class="bg-white p-6 mb-4 shadow-sm">
    <h1 class="text-2xl font-bold text-red-600 text-center uppercase mb-2">
      Sign up for emails & get 25% off
    </h1>
    <p class="text-center text-sm mb-6">
      Plus, you'll be the first to know about sales and events.
    </p>

    <form @submit.prevent="submitForm">
      <!-- Email input -->
      <div class="mb-4">
        <label for="email" class="block text-sm mb-1">email*</label>
        <input 
          type="email" 
          id="email" 
          v-model="email" 
          placeholder="Enter your email address" 
          class="input-field"
          required
        >
      </div>

      <!-- Zip code input -->
      <div class="mb-4">
        <label for="zipCode" class="block text-sm mb-1">zip code* (ex. 12345)</label>
        <input 
          type="text" 
          id="zipCode" 
          v-model="zipCode" 
          placeholder="Enter your zip code" 
          class="input-field"
          pattern="[0-9]{5}"
          required
        >
      </div>

      <!-- Birth date inputs -->
      <div class="mb-4">
        <label class="block text-sm mb-1">birth date</label>
        <div class="flex gap-2">
          <select v-model="birthMonth" class="input-field flex-1" required>
            <option value="" disabled selected>MM</option>
            <option v-for="i in 12" :key="`month-${i}`" :value="i">{{ i }}</option>
          </select>
          <select v-model="birthDay" class="input-field flex-1" required>
            <option value="" disabled selected>DD</option>
            <option v-for="i in 31" :key="`day-${i}`" :value="i">{{ i }}</option>
          </select>
          <select v-model="birthYear" class="input-field flex-1" required>
            <option value="" disabled selected>YYYY</option>
            <option v-for="i in 100" :key="`year-${i}`" :value="currentYear - i">{{ currentYear - i }}</option>
          </select>
        </div>
        <p class="text-xs text-gray-500 mt-1">
          You must be 18 years or older to sign up for emails.
        </p>
      </div>

      <!-- Captcha checkbox -->
      <div class="mb-6">
        <div class="border border-gray-300 p-3 rounded">
          <label class="flex items-center">
            <input type="checkbox" v-model="captchaChecked" class="mr-2">
            <span class="text-sm">I'm not a robot</span>
          </label>
        </div>
      </div>

      <!-- Submit button -->
      <button 
        type="submit" 
        class="btn btn-primary w-full" 
        :disabled="!isFormValid"
        :class="{ 'opacity-50 cursor-not-allowed': !isFormValid }"
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupForm',
  data() {
    return {
      email: '',
      zipCode: '',
      birthMonth: '',
      birthDay: '',
      birthYear: '',
      captchaChecked: false,
      currentYear: new Date().getFullYear()
    }
  },
  computed: {
    isFormValid() {
      // Check if email is valid
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      const isEmailValid = emailRegex.test(this.email);
      
      // Check if zip code is valid (5 digits)
      const zipRegex = /^\d{5}$/;
      const isZipValid = zipRegex.test(this.zipCode);
      
      // Check if birth date is valid and user is at least 18
      const isBirthDateValid = this.birthMonth && this.birthDay && this.birthYear;
      let isOver18 = false;
      
      if (isBirthDateValid) {
        const birthDate = new Date(this.birthYear, this.birthMonth - 1, this.birthDay);
        const today = new Date();
        const ageDate = new Date(today - birthDate);
        const age = Math.abs(ageDate.getUTCFullYear() - 1970);
        isOver18 = age >= 18;
      }
      
      return isEmailValid && isZipValid && isBirthDateValid && isOver18 && this.captchaChecked;
    }
  },
  methods: {
    submitForm() {
      if (this.isFormValid) {
        alert('Form submitted successfully! You will receive your 25% off coupon via email.');
      }
    }
  }
}
</script>
