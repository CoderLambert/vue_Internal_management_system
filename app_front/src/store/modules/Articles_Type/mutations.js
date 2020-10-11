const mutations = {
    // 1 不带参数的方式
    setName (state, payload) {
        state.name = payload.name
    },
    setTypes (state, Types) {
        state.Types = Types
    },
    // setSearch (state, keyWord ) {
    //     state.searhParams.search = keyWord
    // },
    setEditTypeForm (state, EditTypeForm) {
        state.editTypeForm.name = EditTypeForm.name
        state.editTypeForm.id = EditTypeForm.id
        state.editTypeForm.parent = EditTypeForm.parent
    },
    setEditTypeName (state, TypeName) {
        state.editTypeForm.name = TypeName
    },
    setEditTypeParent (state, parent) {
        state.editTypeForm.parent = parent
    },
    // ADD
    setAddTypeName (state, TypeName) {
        state.addTypeForm.name = TypeName
    },
    setAddTypeParent (state, ParentType) {
        state.addTypeForm.parent = ParentType
    },
    
    // Search
    // setSearhParams (state, keyWord) {
    //     state.searhParams.search = keyWord
    // },

    // Dialog 
    showEditTypeDialog (state) {
        state.editTypeDialogVisible = true
    },
    closeEditTypeDialog (state) {
        console.log('closeEditTypeDialog')
        state.editTypeDialogVisible = false
    },
    showAddTypeDialog (state) {
        state.addTypeDialogVisible = true
    },
    closeAddTypeDialog (state) {
        state.addTypeDialogVisible = false
    }
}

export default mutations