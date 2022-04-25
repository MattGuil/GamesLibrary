<template>
    <div class="container">
        <!-- bootswatch CDN -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/flatly/bootstrap.min.css" integrity="sha384-qF/QmIAj5ZaYFAeQcrQ6bfVMAh4zZlrGwTPY7T/M+iTTLJqJBJjwwnsE5Y0mV7QK" crossorigin="anonymous">
        
        <div class="row">
            <div class="col-sm-12">

                <navbar></navbar>

                <alertBox :message="message" :showMessage="showMessage"></alertBox>

                <contenu @isShowing="isShowing($event)" @changeMessage="changeMessage($event)"></contenu>

                <pied></pied>
            
            </div>
        </div>
    </div>
</template>

<script>
import navbar from '../components/navbar/navbar.vue'
import pied from '../components/pied/pied.vue'
import contenu from '../components/contenu/contenu.vue'
import alertBox from '../components/alertBox/alertBox.vue'

export default {
    data() {
        return {
            message: "",
            showMessage: false
        };
    },

    components: {
        navbar,
        pied,
        contenu,
        alertBox
    },

    methods: {
        isShowing(e) {
            this.showMessage = e;
        },

        changeMessage(e) {
            this.message = e;
        }
    }
}
</script>

<style scoped>
    footer {
        margin-bottom: 20px;
    }
</style>
