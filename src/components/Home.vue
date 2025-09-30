<template>
  <div class="home text-center">
    <section class="mb-8">
      <h2 class="text-3xl font-bold mb-4">Welcome to Macy's Presentation</h2>
      <p class="text-lg">This is a demonstration of a Vue.js application for Macy's.</p>
    </section>
    
    <section class="mb-8">
      <h3 class="text-2xl font-semibold mb-4">Featured Products</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 justify-items-center">
        <div v-for="(product, index) in products" :key="index" class="bg-white p-4 rounded shadow">
          <h4 class="text-xl font-medium">{{ product.name }}</h4>
          <p class="text-gray-600">{{ product.description }}</p>
          <p class="text-blue-800 font-bold mt-2">${{ product.price.toFixed(2) }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      products: [
        { 
          name: 'Premium Jacket', 
          description: 'A stylish jacket for all seasons', 
          price: 129.99 
        },
        { 
          name: 'Designer Watch', 
          description: 'Elegant timepiece with premium features', 
          price: 249.99 
        },
        { 
          name: 'Leather Bag', 
          description: 'Handcrafted genuine leather bag', 
          price: 179.99 
        },
        { 
          name: 'Casual Shoes', 
          description: 'Comfortable shoes for everyday wear', 
          price: 89.99 
        },
        { 
          name: 'Silk Scarf', 
          description: 'Luxurious silk scarf with beautiful patterns', 
          price: 59.99 
        },
        { 
          name: 'Designer Sunglasses', 
          description: 'Protect your eyes with style', 
          price: 149.99 
        }
      ]
    }
  }
}
</script>
