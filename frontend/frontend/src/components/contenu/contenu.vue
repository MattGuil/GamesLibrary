<template>
    <div>
        <button id="btnAddGame" type="button" class="btn btn-success" v-b-modal.game-modal>
            Add Game
        </button>
        <table class="table table-hover">
            <!-- Table Head -->
            <thead>
                <tr>
                    <!-- Table header cells -->
                    <th scope="col">Title</th>
                    <th scope="col">Genre</th>
                    <th scope="col">Played?</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="game, index in games" :key="index" :id="game.title">
                    <td>{{ game.title }}</td>
                    <td>{{ game.genre }}</td>
                    <td>
                        <span v-if="game.played">Yes</span>
                        <span v-else>No</span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                            <button :id="game.title" type="button" class="btn btn-info btn-sm" v-b-modal.game-update-modal @click="editGame(game)">
                                Update
                            </button>
                            <button :id="game.title" type="button" class="btn btn-danger btn-sm" @click="deleteGame(game)">
                                Delete
                            </button>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Start of Modal 1 -->
        <b-modal ref="addGameModal"
                    id="game-modal"
                    title="Add a new game"
                    hide-backdrop
                    hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">

                <!-- form group for title entry -->
                <b-form-group id="form-title-group"
                                label="Title:"
                                label-for="form-title-input">
                    <b-form-input id="form-title-input"
                                    type="text"
                                    v-model="addGameForm.title"
                                    required
                                    placeholder="Enter Game">

                    </b-form-input>
                </b-form-group>

                <!-- form group for genre entry -->
                <b-form-group id="form-genre-group"
                                label="Genre:"
                                label-for="form-genre-input">
                    <b-form-input id="form-genre-input"
                                    type="text"
                                    v-model="addGameForm.genre"
                                    required
                                    placeholder="Enter genre">
                        
                    </b-form-input>
                </b-form-group>

                <!-- Checkbox -->
                <b-form-group id="form-played-group">
                    <b-form-checkbox-group v-model="addGameForm.played" id="form-checks">
                        <b-form-checkbox value="true">
                            Played?
                        </b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>

                <!-- buttons : submit and reset -->
                <b-button id="btnSubmit" type="submit" variant="outline-info">Submit</b-button>
                <b-button type="reset" variant="outline-danger">Reset</b-button>

            </b-form>
        </b-modal>
        <!-- End of Modal 1 -->

        <!-- Start of Modal 2 -->
        <b-modal ref="editGameModal"
                    id="game-update-modal"
                    title="Update"
                    hide-backdrop
                    hide-footer>
            <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">

                <!-- form group for title entry -->
                <b-form-group id="form-title-edit-group"
                                label="Title:"
                                label-for="form-title-edit-input">
                    <b-form-input id="form-title-edit-input"
                                    type="text"
                                    v-model="editForm.title"
                                    required
                                    placeholder="Enter Title">

                    </b-form-input>
                </b-form-group>

                <!-- form group for genre entry -->
                <b-form-group id="form-genre-edit-group"
                                label="Genre:"
                                label-for="form-genre-edit-input">
                    <b-form-input id="form-genre-edit-input"
                                    type="text"
                                    v-model="editForm.genre"
                                    required
                                    placeholder="Enter genre">
                        
                    </b-form-input>
                </b-form-group>

                <!-- Checkbox -->
                <b-form-group id="form-played-edit-group">
                    <b-form-checkbox-group v-model="editForm.played" id="form-checks">
                        <b-form-checkbox value="true">
                            Played?
                        </b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>

                <!-- buttons : submit and reset -->
                <b-button id="btnUpdate" type="submit" variant="outline-info">Update</b-button>
                <b-button type="reset" variant="outline-danger">Cancel</b-button>

            </b-form>
        </b-modal>
        <!-- End of Modal 2 -->
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            games: [],
            addGameForm: {
                title: "",
                genre: "",
                played: []
            },
            editForm: {
                id: "",
                title: "",
                genre: "",
                played: []
            }
        }
    },

    methods: {
        // GET Function
        getGames() {
            const path = 'http://localhost:5000/games';
            axios.get(path)
            .then((res) => {
                this.games = res.data.games;
            })
            .catch((err) => {
                console.log(err);
            })
        },

        // POST Function
        addGame(payload) {
            const path = 'http://localhost:5000/games'
            axios.post(path, payload)
            .then(() => {
                this.getGames();
                // For message alert
                this.message = "Game Added!";
                // To show actual message
                this.showMessage = true;
                this.$emit("changeMessage", this.message);
                this.$emit("isShowing", this.showMessage);
            })
            .catch((err) => {
                console.log(err);
                this.getGames();
            })
        },

        initForm() {
            this.addGameForm.title = "";
            this.addGameForm.genre = "";
            this.addGameForm.played = [];
            this.editForm.id = "";
            this.editForm.title = "";
            this.editForm.genre = "";
            this.editForm.played = [];
        },

        // This is for Modal 1 - to submit new game
        onSubmit(e) {
            e.preventDefault();
            this.$refs.addGameModal.hide();
            let played = false;
            if (this.addGameForm.played[0]) played = true;
            const payload = {
                title: this.addGameForm.title,
                genre: this.addGameForm.genre,
                played
            };
            this.addGame(payload);
            this.initForm();
        },

        onReset(e) {
            e.preventDefault();
            this.$refs.addGameModal.hide();
            this.initForm();
        },

        // This is for Modal 2 - to submit updated game
        onSubmitUpdate(e) {
            e.preventDefault();
            this.$refs.editGameModal.hide();
            let played = false;
            if (this.editForm.played[0]) played = true;
                const payload = {
                title: this.editForm.title,
                genre: this.editForm.genre,
                played,
            };
            this.updateGame(payload, this.editForm.id);
        },

        // Handle cancel button click
        onResetUpdate(e) {
            e.preventDefault();
            this.$refs.editGameModal.hide();
            this.initForm();
            this.getGames();
        },

        // Update Individual Game
        updateGame(payload, gameID) {
            const path = `http://localhost:5000/games/${gameID}`;
            axios.put(path, payload)
            .then(() => {
                this.getGames();
                this.message = "Game Updated!";
                this.showMessage = true;
                this.$emit("changeMessage", this.message);
                this.$emit("isShowing", this.showMessage);
            })
            .catch((err) => {
                console.error(err);
                this.getGames();
            });
        },

        // Delete Individual Game
        removeGame(gameID) {
            const path = `http://localhost:5000/games/${gameID}`
            axios.delete(path)
            .then(() => {
                this.getGames();
                this.message = "Game Removed!";
                this.showMessage = true;
                this.$emit("changeMessage", this.message);
                this.$emit("isShowing", this.showMessage);
            })
            .catch((err) => {
                console.error(err);
                this.getGames();
            });
        },

        // Handle update button
        editGame(game) {
            this.editForm = game;
        },

        // Handle delete button
        deleteGame(game) {
            this.removeGame(game.id);
        }
    },

    created() {
        this.getGames();
    }
}
</script>

<style scoped>
    @import './contenu.css'
</style>