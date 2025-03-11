<script setup>
import { onMounted } from "vue";
import { usePlantsStore } from "@/stores/plantsStore";
const plantsStore = usePlantsStore();
import { useRouter } from "vue-router";
const $router = useRouter();

const props = defineProps({
  head: {
    type: Object,
    required: true,
  },
  body: {
    type: Object,
    required: true,
  },
});

const formatPrice = (price) => {
  if (price == null || isNaN(price)) return "0,00";
  return Number(price).toLocaleString("ru-RU", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
};

const goToPlant = (id) => {
  $router.push({name:'plant-detail',params:{id}})
  plantsStore.isTableMode = false
}

</script>

<template>
  <table :class="plantsStore.isTableMode ? 'table table--shadow' : 'table'" v-auto-animate>
    <thead>
      <tr>
        <th v-for="header in head">{{ header }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in body" v-if="!plantsStore.isTableMode">
        <td>{{ item.height }}</td>
        <td>{{ item.pot_size }}</td>
        <td>{{ formatPrice(item.price) }}</td>
      </tr>
      <tr @click="goToPlant(item.id)" v-for="item in body" v-else>
        <td>
          <span>{{ item.species.genus.name }}</span> <br />
          {{ item.species.name }}
        </td>
        <td>{{ item.species.name_latin }}</td>
        <td>от {{ item.min_pot_size }}</td>
        <td> от {{ item.min_height }}</td>
        <td>от {{ formatPrice(item.min_price) }}</td>
        <td>{{ item.species.description }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style src="./Table.scss" scoped />

