<script setup>
import { usePlantsStore } from "@/stores/plantsStore";

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
  descr: {
    type: String,
    required: true,
  },
  sort: {
    type: String,
    required: true,
  },
  nameLatin: {
    type: String,
    required: true,
  },
  height: {
    type: String,
    required: true,
  },
  pot:{
    type: String,
    required: true
  },
  id: {
    type: Number,
    required: true
  },
  img: {
    type: String,
    required: true
  }
});

</script>

<template>
  <div class="card">
    <img :src="img" class="card-img-top" alt="cardImg" v-if="img !== ''" loading="lazy"/>
    <img src="../../assets/images/sample.png"  class="card-img-top" alt="cardImg" v-else loading="lazy"/>
    <div class="card-body d-flex flex-column justify-content-between">
      <h5 class="card-title">{{ name }}</h5>
      <p class="card-text">{{ sort ? sort : nameLatin }}</p>
      <router-link class="card__btn btn btn-primary" :to="/plant/ + id"
        >Узнать больше</router-link
      >
    </div>
  </div>
</template>

<style src="./Card.scss" scoped />
