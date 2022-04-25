<template>
    <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="showMessage">
        <strong>{{ message }}</strong>
        <button type="button" class="close" data-dismiss="alert" aria-label="Close" onclick="function(){showMessage = false;}">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</template>

<script>
export default {
    props: {
        message: String,
        showMessage: Boolean
    }
}
</script>

<style scoped>
    @import './alertBox.css'
</style>