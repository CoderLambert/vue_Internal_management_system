const mutations = {
    // 1 不带参数的方式
    setName (state, payload) {
        state.name = payload.name
    },
    setNotes (state, Notes) {
        state.Notes = Notes
    },
    // setSearch (state, keyWord ) {
    //     state.searhParams.search = keyWord
    // },
    setEditNoteForm (state, EditNoteForm) {
        state.editNoteForm.name = EditNoteForm.name
        state.editNoteForm.id = EditNoteForm.id
    },
    setEditNoteName (state, NoteName) {
        state.editNoteForm.name = NoteName
    },
    // setSearhParams (state, keyWord) {
    //     state.searhParams.search = keyWord
    // },
    showEditNoteDialog (state) {
        state.editNoteDialogVisible = true
    },
    closeEditNoteDialog (state) {
        state.editNoteDialogVisible = false
    },
    // setAddNoteForm (state, AddNoteForm) {
    //     state.addNoteForm.name = AddNoteForm.name
    // },
    showAddNoteDialog (state) {
        state.addNoteDialogVisible = true
    },
    closeAddNoteDialog (state) {
        state.addNoteDialogVisible = false
    },
    setAddNoteName (state, NoteName) {
        state.addNoteForm.name = NoteName
    }

}

export default mutations