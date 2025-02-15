<script setup>
    import DownloadSvg from '../../assets/images/download.svg';
</script>

<template>
    <div class="file">
        <DownloadSvg class="file__svg"/>
        <p class="file__name">File name</p>
        <button class="file__btn btn">Скачать</button>
    </div>
</template>

<style src="./File.scss" scoped />

