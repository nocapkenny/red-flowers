<script setup>
import Card from "../Card/Card.vue";
const props = defineProps({
  isBigCard: {
    type: Boolean,
    default: false,
    required: true
  },
})


const cards = [1, 2, 3, 4, 5, 6, 7];
</script>

<template>
  <div class="container text-center">
    <div class="row row-cols-1 row-cols-md-4 g-4" v-auto-animate>
      <div class="col" v-for="card in cards" :key="card">
        <Card :isBigCard="isBigCard"/>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
