<template>
  <div class="container-center">
    <div class="bg-white p-6 mb-4 shadow-sm max-w-md w-full">
      <h1 class="text-2xl font-bold text-red-600 text-center uppercase mb-2">
        Create your account
      </h1>
      <p class="text-center text-sm mb-6">
        Join us to access exclusive offers and features
      </p>

      <div v-if="registrationSuccess" class="mb-4 p-3 bg-green-100 text-green-700 rounded text-center">
        <p>{{ successMessage }}</p>
        <p class="mt-2">
          <router-link to="/signin" class="text-red-600 underline">Sign in now</router-link>
        </p>
      </div>

      <form v-else @submit.prevent="register">
        <!-- Name input -->
        <div class="mb-4">
          <label for="name" class="block text-sm mb-1">full name*</label>
          <input 
            type="text" 
            id="name" 
            v-model="name" 
            placeholder="Enter your full name" 
            class="input-field"
            required
          >
        </div>

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
          <p v-if="emailError" class="text-xs text-red-500 mt-1">
            {{ emailError }}
          </p>
        </div>

        <!-- Password input -->
        <div class="mb-4">
          <label for="password" class="block text-sm mb-1">password*</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            placeholder="Create a password" 
            class="input-field"
            required
          >
          <p class="text-xs text-gray-500 mt-1">
            Password must be at least 8 characters with uppercase, lowercase, number, and special character.
          </p>
          <p v-if="passwordError" class="text-xs text-red-500 mt-1">
            {{ passwordError }}
          </p>
        </div>

        <!-- Confirm Password input -->
        <div class="mb-6">
          <label for="confirmPassword" class="block text-sm mb-1">confirm password*</label>
          <input 
            type="password" 
            id="confirmPassword" 
            v-model="confirmPassword" 
            placeholder="Confirm your password" 
            class="input-field"
            required
          >
          <p v-if="confirmPasswordError" class="text-xs text-red-500 mt-1">
            {{ confirmPasswordError }}
          </p>
        </div>

        <!-- Error message -->
        <div v-if="errorMessage" class="mb-4 p-2 bg-red-100 text-red-700 text-sm rounded">
          {{ errorMessage }}
        </div>

        <!-- Submit button -->
        <button 
          type="submit" 
          class="btn btn-primary w-full" 
          :disabled="isLoading || !isFormValid"
          :class="{ 'opacity-50 cursor-not-allowed': isLoading || !isFormValid }"
        >
          {{ isLoading ? 'Creating Account...' : 'Register' }}
        </button>
      </form>

      <div class="mt-4 text-center text-sm">
        <p>Already have an account? <router-link to="/signin" class="text-red-600">Sign in</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import AuthService from '../services/auth.service';

export default {
  name: 'Register',
  data() {
    return {
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      isLoading: false,
      errorMessage: '',
      emailError: '',
      passwordError: '',
      confirmPasswordError: '',
      registrationSuccess: false,
      successMessage: ''
    }
  },
  computed: {
    isFormValid() {
      // Basic validation
      if (!this.name || !this.email || !this.password || !this.confirmPassword) {
        return false;
      }
      
      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.email)) {
        this.emailError = 'Please enter a valid email address';
        return false;
      } else {
        this.emailError = '';
      }
      
      // Password validation (at least 8 chars, uppercase, lowercase, number, special char)
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;
      if (!passwordRegex.test(this.password)) {
        this.passwordError = 'Password does not meet requirements';
        return false;
      } else {
        this.passwordError = '';
      }
      
      // Confirm password validation
      if (this.password !== this.confirmPassword) {
        this.confirmPasswordError = 'Passwords do not match';
        return false;
      } else {
        this.confirmPasswordError = '';
      }
      
      return true;
    }
  },
  methods: {
    async register() {
      if (!this.isFormValid) return;
      
      this.isLoading = true;
      this.errorMessage = '';
      
      // Debug log
      console.log('Attempting to register with:', {
        name: this.name,
        email: this.email,
        password: '********' // Don't log actual password
      });
      
      try {
        console.log('Calling AuthService.register...');
        const result = await AuthService.register(this.name, this.email, this.password);
        console.log('Registration result:', result);
        
        if (result.success) {
          this.registrationSuccess = true;
          this.successMessage = result.message || 'Registration successful! Please check your email to activate your account.';
        } else {
          this.errorMessage = result.message || 'Registration failed. Please try again.';
          
          // Handle specific error cases
          if (result.message && result.message.includes('email')) {
            this.emailError = result.message;
          } else if (result.message && result.message.includes('senha') || result.message && result.message.includes('password')) {
            this.passwordError = result.message;
          }
        }
      } catch (error) {
        console.error('Registration error:', error);
        this.errorMessage = 'An error occurred. Please try again.';
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>
