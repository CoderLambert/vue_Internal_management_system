const Strategies = {
    isEmpty: function ( value, errorMsg) {
        if (value.length === 0 || value === '') {
            return errorMsg
        }
    },
    minLength: function ( value, length, errorMsg) {
        if (value.length < length) {
            return errorMsg
        }
    },
    maxLength: function ( value, length, errorMsg) {
        if (value.length > length) {
            return errorMsg
        }
    },
    isMobile: function ( value, errorMsg) {
        if (!/(^1[3|5|8][0-9]{9}$)/.test(value)) {
            return errorMsg
        }
    }
}

class Validator {
    constructor () {
        this.cache = []
        this.strategies = Strategies
    }
    add (formValue, rules) {
        let self = this
        for (let i = 0, rule; i < rules.length;) {
            rule = rules[i]
            i++
            ( function (rule) {
                let strategyAry = rule.strategy.split(':')
                let errorMsg = rule.errorMsg
                self.cache.push( function () {
                    let strategy = strategyAry.shift()
                    strategyAry.unshift(formValue)
                    strategyAry.push(errorMsg)
                    return self.strategies[strategy].apply(formValue, strategyAry)
                })
            })(rule)
        }
    }
    validation () {
        for (let i = 0, validatorFunc; i < this.cache.length; i++) {
            validatorFunc = this.cache[i]
            let errorMsg = validatorFunc()
            if (errorMsg) {
                return errorMsg
            }
        }
    }
}

export default Validator