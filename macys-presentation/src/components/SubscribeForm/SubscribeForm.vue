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
          <select v-model="birthMonth" class="input-field flex-1">
            <option :value="null" disabled>MM</option>
            <option v-for="i in 12" :key="`month-${i}`" :value="i">{{ i }}</option>
          </select>
          <select v-model="birthDay" class="input-field flex-1">
            <option :value="null" disabled>DD</option>
            <option v-for="i in 31" :key="`day-${i}`" :value="i">{{ i }}</option>
          </select>
          <select v-model="birthYear" class="input-field flex-1">
            <option :value="null" disabled>YYYY</option>
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

      <!-- Success message -->
      <div v-if="isSubmitted" class="mb-4 p-3 bg-green-100 text-green-700 rounded text-center">
        Thank you for signing up! You will receive your 25% off coupon via email.
      </div>
      
      <!-- Submit button -->
      <button 
        v-if="!isSubmitted"
        type="submit" 
        class="btn btn-primary w-full" 
        :disabled="!isFormValid || isLoading"
        :class="{ 'opacity-50 cursor-not-allowed': !isFormValid || isLoading }"
      >
        {{ isLoading ? 'Submitting...' : 'Submit' }}
      </button>
        <div class="bg-white p-6 shadow-sm">
    <h2 class="text-xl font-bold text-center uppercase mb-4">
      Sign up for texts, too!
    </h2>
    
    <p class="text-center mb-4">
      Text <strong>MAGIC</strong> to <strong>62297</strong> to start receiving message alerts today!
    </p>
    
    <div class="text-xs text-gray-600 space-y-2">
      <p>
        By texting the keyword MAGIC, you consent to receive recurring marketing automated text messages
        from Macy's to your mobile number. Consent is not required as a condition of any purchase. Message & data rates may apply.
      </p>
      
      <p>
        Message frequency varies. Msg & data rates may apply. Text HELP for help, STOP to cancel. 
        View our <a href="#" class="text-red-600 underline">Terms & Conditions</a> and <a href="#" class="text-red-600 underline">Privacy Practices</a>.
      </p>
      
      <p>
        Supported carriers: AT&T, T-Mobile, Verizon Wireless, Sprint, Boost, Cricket, MetroPCS, U.S. Cellular, and others.
      </p>
    </div>
  </div>
    </form>
  </div>
</template>

<script>
import AuthService from '../../services/auth.service.js';

export default {
  name: 'SubscribeForm',
  data() {
    return {
      email: '',
      zipCode: '',
      birthMonth: null,
      birthDay: null,
      birthYear: null,
      captchaChecked: false,
      currentYear: new Date().getFullYear(),
      isLoading: false,
      isSubmitted: false
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
        const age = Math.floor((today - birthDate) / (365.25 * 24 * 60 * 60 * 1000));
        isOver18 = age >= 18;
      }
      
      // DIAGNOSTIC LOGGING - Remove after debugging
      console.log('=== Form Validation Debug ===');
      console.log('Email:', this.email, '| Valid:', isEmailValid);
      console.log('Zip Code:', this.zipCode, '| Valid:', isZipValid);
      console.log('Birth Date:', { month: this.birthMonth, day: this.birthDay, year: this.birthYear });
      console.log('Birth Date Valid:', isBirthDateValid);
      if (isBirthDateValid) {
        const birthDate = new Date(this.birthYear, this.birthMonth - 1, this.birthDay);
        const today = new Date();
        const age = Math.floor((today - birthDate) / (365.25 * 24 * 60 * 60 * 1000));
        console.log('Birth Date Object:', birthDate);
        console.log('Today:', today);
        console.log('Calculated Age:', age);
      }
      console.log('Is Over 18:', isOver18);
      console.log('Captcha Checked:', this.captchaChecked);
      console.log('Final isFormValid:', isEmailValid && isZipValid && isBirthDateValid && isOver18 && this.captchaChecked);
      console.log('===========================');
      
      return isEmailValid && isZipValid && isBirthDateValid && isOver18 && this.captchaChecked;
    }
  },
  methods: {
    async submitForm() {
      if (this.isFormValid) {
        this.isLoading = true;
        
        // Collect the form data
        const formData = {
          email: this.email,
          zipCode: this.zipCode,
          birthDate: `${this.birthYear}-${this.birthMonth.toString().padStart(2, '0')}-${this.birthDay.toString().padStart(2, '0')}`
        };
        
        // Log the data to console
        console.log('Sending email subscribe data:', formData);
        
        try {
          // Call the real API
          const response = await AuthService.subscribe(
            formData.email,
            formData.zipCode,
            formData.birthDate
          );
          
          // Log the response
          console.log('Email subscribe response:', response);
          
          if (response.success) {
            // Handle successful response
            this.isSubmitted = true;
            
            // Display coupon code to user
            alert(`Thank you for subscribing! Your coupon code is: ${response.coupon_code}`);
            
            // Reset form after successful submission
            this.email = '';
            this.zipCode = '';
            this.birthMonth = null;
            this.birthDay = null;
            this.birthYear = null;
            this.captchaChecked = false;
          } else {
            // Handle error response
            alert(response.message || 'An error occurred. Please try again.');
          }
        } catch (error) {
          console.error('Error submitting form:', error);
          alert('An error occurred. Please try again.');
        } finally {
          this.isLoading = false;
        }
      }
    }
  }
}
</script>
