<template>
  <div class="home_container">
    <el-container>
      <el-header>图书馆</el-header>
      <el-main>
        <!-- 添加书籍按钮 -->
        <div style="text-align:center">
          <el-button type="primary" @click="addBookVisible = true" round>添加书籍</el-button>
        </div>

        <!-- 书籍表格 -->
        <div style="margin-top:20px; width:700px">
          <el-table :data="books" style="width: 100%">
            <el-table-column label="书名" width="180">
              <template slot-scope="scope">
                <i class="el-icon-reading"></i>
                <span style="margin-left: 10px">{{ scope.row.title }}</span>
              </template>
            </el-table-column>
            <el-table-column label="作者" width="180">
              <template slot-scope="scope">
                <i class="el-icon-user-solid"></i>
                <span style="margin-left: 10px">{{ scope.row.author }}</span>
              </template>
            </el-table-column>
            <el-table-column label="是否已读" width="180">
              <template slot-scope="scope">
                <span style="margin-left: 10px">
                  <el-button type="primary" v-if="scope.row.read">已读</el-button>
                  <el-button type="danger" v-else>未读</el-button>
                </span>
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="mini" @click="showEditDialog(scope.row.id)">编辑</el-button>
                <el-button size="mini" type="danger" @click="deleteBook(scope.row.id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-main>
    </el-container>

    <!-- 添加书籍对话框 -->
    <el-dialog title="添加书籍" :visible.sync="addBookVisible" width="30%" @close="addDialogClosed">
      <el-form ref="bookRef" :model="addBookForm" :rules="addBookRules" label-width="80px">
        <el-form-item label="书籍名称" prop="title">
          <el-input v-model="addBookForm.title"></el-input>
        </el-form-item>
        <el-form-item label="作者名称" prop="author">
          <el-input v-model="addBookForm.author"></el-input>
        </el-form-item>
        <el-form-item label="是否读过">
          <el-switch v-model="addBookForm.read"></el-switch>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="addBookVisible = false">取 消</el-button>
        <el-button type="primary" @click="addBook">确 定</el-button>
      </span>
    </el-dialog>

    <!--编辑对话框 -->
    <el-dialog title="编辑" :visible.sync="editBookVisible" width="30%" @close="editDialogClosed">
      <el-form ref="editFormRef" :model="editForm" :rules="addBookRules" label-width="80px">
        <el-form-item label="书籍名称" prop="title">
          <el-input v-model="editForm.title"></el-input>
        </el-form-item>
        <el-form-item label="作者名称" prop="author">
          <el-input v-model="editForm.author"></el-input>
        </el-form-item>
        
        <el-form-item label="是否读过">
          <el-switch v-model="editForm.read" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
        </el-form-item>

      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="editBookVisible = false">取 消</el-button>
        <el-button @click="editBookInfo">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 存放后端的书籍
      books: [],
      // 添加书籍的对话框
      addBookVisible: false,
      // 存放添加书籍表格数据
      addBookForm: {
        title: "",
        author: "",
        read: false
      },
      // 添加书籍规则
      addBookRules: {
        title: [{ required: true, message: "请输入书籍名称", trigger: "blur" }],
        author: [{ required: true, message: "请输入作者名称", trigger: "blur" }]
      },
      // 编辑书籍对话框
      editBookVisible: false,
      // 存放编辑书籍的对象
      editForm: {}
    };
  },
  methods: {
    async getBooks() {
      // 获取书籍
      const res = await this.$http.get("books");
      // console.log(res);
      // console.log(res.status)
      // console.log(res.status)
      this.books = res.data;
    },
    addBook() {
      this.$refs.bookRef.validate(async valid => {
        if (!valid) return;
        //添加书籍请求
        const res = await this.$http.post("add", this.addBookForm);
        console.log(res);
        if (res.status !== 200) {
          this.$message.error("添加书籍失败");
        }
        this.$message.success("添加书籍成功");
        this.addBookVisible = false;
        this.getBooks();
      });
    },
    // 清空添加书籍输入框
    addDialogClosed() {
      this.$refs.bookRef.resetFields();
    },

    // 编辑书籍对话框
    async showEditDialog(id) {
      // console.log(id)
      const res = await this.$http.get("showbooks/" + id);
      // 看res.data 会发现出现了 __ob__: Observer
      // 这是vue 里的特性
      console.log(res);
      console.log(res.data[0]);
      if (res.status !== 200) {
        return this.$message.error("查询书籍失败");
      }
      // 带 [0] 可以才能获得数据
      this.editForm = res.data[0];

      this.editBookVisible = true;
    },
    // 监听书籍修改对话框的关闭事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields();
    },
    // 修改书籍信息
    editBookInfo() {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) return;
        console.log(this.editForm);
        const res = await this.$http.post(
          "editbooks/" + this.editForm.id,
          this.editForm
        );
        console.log(res);
        if (res.status !== 200) {
          return this.$message.error("修改失败");
        }

        //关闭对话框 刷新页面 提示修改成功
        this.editBookVisible = false;
        this.getBooks();
        this.$message.success("修改成功");
      });
    },
    // 删除书籍 根据id值
    async deleteBook(id) {
      // 弹框提示用户删除书籍
      const res = await this.$confirm(
        "此操作将永久删除该书籍, 是否继续?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        }
      ).catch(err => err);
      // 如果用户确认删除 则返回confirm 取消返回cancel

      if (res !== "confirm") {
        return this.$message.info("已取消删除");
      }

      const res2 = await this.$http.post("delete/" + id);
      if (res2.status !== 200) {
        return this.$message.error("删除失败");
      }

      this.getBooks();
      return this.$message.success("删除成功");
    }
  },

  created() {
    this.getBooks();
  }
};
</script>

<style lang="less" scoped>
.home_container {
  background-color: #fff2df;
  height: 100%;
}
.el-header {
  text-align: center;
  font-size: 40px;
  margin-top: 20px;
}
.el-main {
  margin: 0 auto;
}
</style>