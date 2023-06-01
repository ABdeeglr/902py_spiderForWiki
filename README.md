# README

spider for catch certain pictures in wiki

## Step 01 图片链接准备阶段


1. 从 wiki 数据表中挖掘出全部角色信息
2. 基于角色名生成需要访问的二级页面
3. 遍历所有二级页面，获取全部 HTML 资源
4. 对 HTML 资源解析, 获取全部图片链接
5. 处理上述数据, 将角色及其图片链接通过 Json 格式文件储存
## Step 02 图片获取阶段

1. 针对每个角色进行异步处理
2. 获取某个角色的立绘图片，并存储到对应文件夹
3. 获取角色涉及的过场图片，存储到指定文件夹

