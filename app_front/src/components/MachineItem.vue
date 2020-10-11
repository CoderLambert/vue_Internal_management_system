<template>
  <div>
    <el-tabs type="border-card">
        <el-tab-pane  v-for="(projectList,key) in MachineProjectList"  v-bind:key = "key" :label="key">
            <div class="machine-box">
                <el-card class="machine-item-container" v-for="(machine,index) in projectList" v-bind:key = "index" shadow="hover">
                    <div slot="header" class="clearfix">
                        <span class="machine-owner">所属人员</span>
                        <span class="machine-owner-name">  {{machine.username}}</span>
                        <el-button
                                icon="el-icon-delete" circle
                                style="float: right;"
                                size="mini"
                                type="danger"
                                @click="emitDeleteMachine(machine)"
                        >
                        </el-button>
                        <el-button style="float: right;margin-right:5px"
                            icon="el-icon-edit" circle
                            size="mini"
                            type="primary"
                            @click="emitEditMachineInfo(machine)"
                        >
                        </el-button>
                    </div>

                    <div class="machine-item-body">
                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    BMC IP 
                                </div>
                                <div class="machine-item-info">
                                    <el-tooltip content="复制IP" placement="bottom" effect="light">

                                    <span  v-if="machine.BMC_ip"
                                        v-clipboard:copy="machine.BMC_ip"
                                        v-clipboard:success="onCopy"
                                        v-clipboard:error="onError"
                                        class="svn-copy"
                                    >
                                    {{ machine.BMC_ip }}
                                    </span>
                                    </el-tooltip>
                                        <el-tag size="mini" 
                                            style="cursor: pointer;margin-left:10px"  
                                            @click="open_link(`http://${machine.BMC_ip}`)"
                                        > 
                                            http
                                        </el-tag>
                                        <el-tag size="mini" 
                                            type="success"
                                            style="cursor: pointer;margin-left:10px"  
                                            @click="open_link(`https://${machine.BMC_ip}`)"
                                        > 
                                            https
                                        </el-tag>
                            
                                    <!-- </el-tooltip> -->

                                </div>
                            </div>
                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    UserName
                                </div>
                                <div class="machine-item-info">
                                    <el-tooltip content="单击复制用户名" placement="bottom" effect="light">

                                    <span  v-if="machine.web_username"
                                        v-clipboard:copy="machine.web_username"
                                        v-clipboard:success="onCopy"
                                        v-clipboard:error="onError"
                                        class="svn-copy"
                                    >
                                    {{ machine.web_username }}
                                    </span>
                                    </el-tooltip>
                                </div>
                            </div>
                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    Password
                                </div>
                                <div class="machine-item-info">
                                    <!-- {{machine.web_password}} -->
                                    <el-tooltip content="单击复制密码" placement="bottom" effect="light">
                                    <span  v-if="machine.web_password"
                                        v-clipboard:copy="machine.web_password"
                                        v-clipboard:success="onCopy"
                                        v-clipboard:error="onError"
                                        class="svn-copy"
                                    >
                                    {{ machine.web_password }}
                                    </span>
                                    </el-tooltip>

                                </div>
                            </div>

                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    Host IP
                                </div>
                                <div class="machine-item-info">
                                    {{machine.Host_ip}}
                                </div>
                            </div> 
                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    当前使用状态
                                </div>
                                <div class="machine-item-info">
                                    <el-tag v-if="machine.current_state === 1" type="success" size="">
                                       {{MachineStates[machine.current_state-1].state}} 
                                    </el-tag>
                                    <el-tag v-if="machine.current_state === 2" type="warning">
                                       {{MachineStates[machine.current_state-1].state}} 
                                    </el-tag>
                                    <el-tag v-if="machine.current_state === 3" type="danger">
                                       {{MachineStates[machine.current_state-1].state}} 
                                    </el-tag>                                    

                                </div>
                            </div> 
                            <div class="machine-item-row" v-show="machine.current_state === 2 || machine.current_state === 3" >
                                <div class="machine-item-title">
                                    起始时间
                                </div>
                                <div class="machine-item-info">
                                    {{machine.start_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss')}}
                                </div>
                            </div> 

                            <div class="machine-item-row" v-show="machine.current_state === 2 || machine.current_state === 3">
                                <div class="machine-item-title">
                                    结束时间
                                </div>
                                <div class="machine-item-info">
                                    {{machine.end_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss')}}
                                </div>
                            </div> 
                            <div class="machine-item-row">
                                <div class="machine-item-title">
                                    备注
                                </div>
                            </div>   
                            <div class="machine-item-row">
                                <div class="machine-item-remark">
                                    <p class="machine-item-remark-content">
                                        {{ machine.description }}
                                    </p>
                                </div>
                            </div>

                    </div>                       
                </el-card>                    
            </div>
        </el-tab-pane>
    </el-tabs>
    
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'MachineItem',
  data () {
    return {
        activeNames: [1]
    }
  },
  computed: {
      MachineProjectList () {
        return this._.groupBy(this.MachineInfo, 'project')
      } 
  },
  mounted () {
  },
  beforeDestroy () {
  },
  
  props: {
      MachineInfo: Array,
      MachineStates: Array,
      default: []
  },
  methods: {
    onCopy (e) {
      this.$message.success(`已复制 ${e.text} 到粘贴板`)
    },
    onError: function (e) {
      this.$message.error('复制失败！')
    },
    open_link (URL) {
    //   console.log(URL)
      window.open(URL)
    },
    emitEditMachineInfo (machineInfo) {
        console.log('EditMachineInfo')
        console.log(machineInfo)
        this.$emit('EditMachineInfo', machineInfo)
    },
    emitDeleteMachine (machineInfo) {
        this.$emit('DeleteMachine', machineInfo)
    }

  },
  components: {

  }
}
</script>

<style lang="less" scoped>
.machine-project-title {
    // background-color: skyblue;
    width: 100%;
    padding:5px;
    font-size: 32px;
    color: skyblue;
    font-weight: 620;
    
}
.machine-box {
    display: flex;
    // 默认情况下，项目都排在一条线（又称"轴线"）上。
    // flex-wrap属性定义，如果一条轴线排不下，如何换行。
    // flex-wrap: nowrap | wrap | wrap-reverse;
    flex-wrap: wrap; 
    // justify-content属性定义了项目在主轴上的对齐方式。
    justify-content: flex-start;
    .machine-item-container {
        // width: 450px;
        height: 500px;
        margin: 5px;

        .machine-item-row {
            display: flex;
            align-items: center;
            margin-bottom:15px;
            overflow: auto;

            .machine-item-title {
                width: 120px;
                // float: left;
                border: 1px solid #efefef;
                text-align: center;
                font-size: 14px;
                color: grey;
                font-weight: 600;
                padding:0 4px;
                background: aliceblue;
            }
            .machine-item-info {
                font-size: 14px;
                padding-left: 25px;                
            }
            .machine-item-remark {
                width: 100%;
                height: 120px;
                // min-height: 200px;
                background:#f5f7fa;
                overflow: auto;
                /*核心代码*/
                &::-webkit-scrollbar {
                    /*滚动条整体样式*/
                    width: 4px;
                    /*高宽分别对应横竖滚动条的尺寸*/
                    height: 4px;
                }

                &::-webkit-scrollbar-thumb {
                    /*滚动条里面小方块*/
                    border-radius: 5px;
                    -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
                    background: rgba(0, 0, 0, 0.2);
                }

                &::-webkit-scrollbar-track {
                    /*滚动条里面轨道*/
                    -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
                    border-radius: 0;
                    background: rgba(0, 0, 0, 0.1);
                }

                .machine-item-remark-content {
                    font-size: 12px;
                    white-space:pre-wrap;
                    word-wrap:break-word;
                    padding: 10px;
                }
            }   
        }
    }
    // 小于 780px  则宽度为一半 
    @media only screen and (max-width: 800px) {
        .machine-item-container {
            width: 45%;
        } 
    }

    @media  screen and (min-width: 801px) and (max-width: 1606px) {
        .machine-item-container {
            width: 32%;
        } 
    }

    @media only screen and (min-width: 1607px) {
        .machine-item-container {
            width: 32%;
        }
    }

    .machine-owner {
        font-size: 14px;
        color: #606266;
        border: 1px solid #efefef;
        border-radius: 5px;
        padding: 2px;  
        width: 120px;
        text-align: center;  
        background:#f5f7fa;   
    }
    .machine-owner-name {
        font-size: 14px;
        color: #606266; 
        margin-left: 15px;
        text-align: center;     
    } 
}
</style>
