<template>
  <footer class="bg-gray-50 pt-8 pb-4 border-t border-gray-200">
    <div class="container-center">
      <!-- Footer links -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8">
        <!-- Customer Service -->
        <div>
          <h3 class="font-bold mb-3 text-sm">Customer Service</h3>
          <ul class="text-xs space-y-2">
            <li><a href="#" class="hover:underline">Help & FAQs</a></li>
            <li><a href="#" class="hover:underline">Orders</a></li>
            <li><a href="#" class="hover:underline">Shipping</a></li>
          </ul>
        </div>

        <!-- Credit Card -->
        <div>
          <h3 class="font-bold mb-3 text-sm">Macy's Credit Card</h3>
          <ul class="text-xs space-y-2">
            <li><a href="#" class="hover:underline">Apply for Macy's Credit Card</a></li>
            <li><a href="#" class="hover:underline">Cardholder Benefits</a></li>
          </ul>
        </div>

        <!-- Stores & Services -->
        <div>
          <h3 class="font-bold mb-3 text-sm">Stores & Services</h3>
          <ul class="text-xs space-y-2">
            <li><a href="#" class="hover:underline">Catalogs & Forms</a></li>
            <li><a href="#" class="hover:underline">Locations & Hours</a></li>
          </ul>
        </div>

        <!-- Macy's Inc -->
        <div>
          <h3 class="font-bold mb-3 text-sm">Macy's Inc.</h3>
          <ul class="text-xs space-y-2">
            <li><a href="#" class="hover:underline">Corporate Sales</a></li>
            <li><a href="#" class="hover:underline">Macy's.com Site</a></li>
          </ul>
        </div>
      </div>

      <!-- Social media icons -->
      <div class="flex justify-center space-x-4 border-t border-gray-200 pt-4">
        <a href="#" aria-label="Facebook">Facebook</a>
        <a href="#" aria-label="Instagram">Instagram</a>
        <a href="#" aria-label="Twitter">Twitter</a>
      </div>

      <!-- Copyright -->
      <div class="text-xs text-gray-500 text-center pt-4">
        <p>&copy; 2025 Macy's. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>