const mutations = {
    changeOrderingDirection (state) {
        if ( state.orderingDirection === '-' ) {
            state.orderingDirection = ''
        } else {
            state.orderingDirection = '-'
        }
        // state.commit('setOrderOrdering')
        // state.orderingDirection = state.orderingDirection === '-' ? '' : '-'
        // state.orderMessage = state.orderingDirection === '-' ? '升序' : '降序'
    },

    changeOrderingOrderMessage (state) {
        if ( state.orderMessage === '升序' ) {
            state.orderMessage = '降序'
        } else {
            state.orderMessage = '升序'
        }
    },
    
    changeOrdering (state) {
        state.quuery_params.ordering = state.orderingDirection + state.orderCondition
    },

    setOrderCondition (state, value) {
        state.orderCondition = value
    },

    // setOrderOrdering (state) {
    //     state.orderOrdering = state.orderingDirection + state.orderCondition
    // },
    setArticles (state, value) {
        state.articles = value
    },
    
    setTotalCount (state, value) {
        state.total_count = value
    },
    setQuueryParamsTypes (state, value) {
        state.quuery_params.types = value
    },

    setQuueryParamsPageNum (state, value) {
        state.quuery_params.pagenum = value
    },

    setQuueryParamsPageSize (state, value) {
        state.quuery_params.pagesize = value
    },

    setQuueryParamsUser (state, value) {
        state.quuery_params.user = value
    },
    
    setQuueryParamsNote (state, value) {
        state.quuery_params.note = value
    },

    setQuueryParamsSearch (state, value) {
        state.quuery_params.search = value
    },
    QuueryParamsreset (state, value ) {
        state.quuery_params = value
    }

}

export default mutations