<template>
  <div class="container-center">
    <SignupForm />
    <SmsSignup />
  </div>
</template>

<script>
import SignupForm from '../components/SignupForm/SignupForm.vue';
import SmsSignup from '../components/SmsSignup/SmsSignup.vue';

export default {
  name: 'SignupPage',
  components: {
    SignupForm,
  }
}
</script>