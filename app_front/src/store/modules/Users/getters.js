const getters = {
    // 1 不带参数的getters
    formatName: state => {
        let postfix = 'formater '
        return state.name + postfix
    }
}

export default getters
