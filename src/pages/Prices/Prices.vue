<script setup>
import Header from "../../components/Header/Header.vue";
import File from "../../components/File/File.vue";
import { usePriceStore } from "@/stores/pricesStore";
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
const pricesStore = usePriceStore();
const { prices } = storeToRefs(pricesStore);
import { useHead } from "@vueuse/head";

useHead({
  title: 'Питомник "Красная Гвоздика"',
  meta: [
    { name: "description", content: 'питомник растений "Красная Гвоздика"' },
    {
      name: "keywords",
      content:
        "цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения",
    },
  ],
});

onMounted(() => {
  pricesStore.getPrices();
});
</script>

<template>
  <Header />
  <section class="prices">
    <div class="prices__box" v-auto-animate>
      <h3 class="prices__title title">Прайс-лист</h3>
      <p class="prices__text">
        Внимание! Уважаемые клиенты! В текущей ситуации цены, указанные на
        сайте, не являются официальной офертой: цены могут меняться в
        зависимости от ситуации на рынке. Чтобы выяснить актуальные цены,
        обращайтесь к специалистам питомника.
      </p>
      <div class="prices__files"  v-if="prices">
        <File
          v-for="file in prices"
          :key="file.id"
          :file-path="file.file"
          :file-name="file.name"
          :is-active="file.is_active"
        />
      </div>
    </div>
  </section>
</template>

<style src="./Prices.scss" scoped />
