// Vue.filter('UTCDateFormat', function ( dataStr, pattern = 'YYYY-MM-DD HH:mm:ss' ) {
//     return moment.parseZone(dataStr).local().format(pattern)
//   })
  
//   Vue.filter('ArticalDetailFormat', function ( artical_id ) {
//     return `/article/${artical_id}`
//   })
import moment from 'moment'

export const UTCDateFormat = (dataStr, pattern = 'YYYY-MM-DD HH:mm:ss') => {
    return moment.parseZone(dataStr).local().format(pattern)
}
export const ArticalDetailFormat = artical_id => {
    return `/article/${artical_id}`
}
