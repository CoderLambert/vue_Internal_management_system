// 用户名正则，4到16位（字母，数字，下划线，减号）
var reUserName = /^[a-zA-Z0-9_-]{3,16}$/

// 最短8位，最长16位 {8,16}
// 最少必须包含1个数字
// 最少必须包含2个小写字母
// 最少必须包含2个大写字母
// 最少必须包含1个特殊字符
var rePassword = /^.*(?=.{8,16})(?=.*\d)(?=.*[A-Z]{2,})(?=.*[a-z]{2,})(?=.*[!@#$%^&*?(),.;:'"<>{}[]\/+-=|_]).*$/
// 链接：https://www.jianshu.com/p/726f6e4a5714

// 11位手机号
const reMobilePhone = /^1[3|4|5|7|8][0-9]\d{8}$/

// 座机和传真格式是一样的：区号-号码
const reTelephone = /^(\d{3,4}-)?\d{7,8}$/

// 邮箱  以数字字母开头，中间可以是多个数字字母下划线或"_"  然后是"@"符号，后面是数字字母  然后是"."符号2-4个字母结尾
// 此处考虑canco邮箱格式  lizhi1@cancon.com.cn  做了补充 (\.[a-zA-Z]{2,6})?
// 参考 http://c.biancheng.net/view/5632.html
const reEmail = /^([a-zA-Z]|[0-9])(\w|-|_)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,6})(\.[a-zA-Z]{2,6})?$/
//  /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/

// 身份证
const reIDC = /^\d{6}(18|19|20)?\d{2}(0[1-9]|1[0-2])(([0-2][1-9])|10|20|30|31)\d{3}(\d|X|x)$/

// 验证中文
const reChiniseWord = /^[\u0391-\uFFE5]+$/

// 验证邮编：
const rePostcode = /^\d{6}$/

// 范围0~9999小数点后1~2位
// var reg = /^-?\d{1,4}(?:\.\d{1,2})?$/;

var RegValid = {
  isUserName (data) {
    return reUserName.test(data)
  },
  isPassword (data) {
    return rePassword.test(data)
  },

  isEmail (data) {
    return reEmail.test(data)
  },
  isIDC (data) {
    return reIDC.test(data)
  },
  isTelephone (data) {
    return reTelephone.test(data)
  },
  isMobilePhone (data) {
    return reMobilePhone.test(data)
  },
  isChiniseWord (data) {
    return reChiniseWord.test(data)
  },
  isPostcode (data) {
    return rePostcode.test(data)
  }
}

export default RegValid
