const state = {
  articles: [],
  total_count: null,
  orderConditions: [
      { name: 'original', title: '原创' },
      { name: 'public', title: '公开' },
      { name: 'browse_num', title: '浏览次数' },
      { name: 'add_time', title: '发布时间' }
    ],
    orderingDirection: '-',
    orderCondition: 'add_time',
    orderMessage: '升序',
    // order
    quuery_params: {
            note: '',
            types: null,
            user: '',
            search: '',
            pagenum: 1,
            pagesize: 10,
            ordering: '-add_time'
    }
}
export default state
