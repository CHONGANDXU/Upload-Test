# Vue
1. Vue组件通信，父传子-用什么传递数据，关键字段是什么

2. Vue里绑定事件的方法有哪些？

3. MVVM框架由那几部分构成

4. Vue.js 的核心是什么？

5. Vue中路由实现什么功能，由哪个模块实现？

6. css和html的样式有什么不同

7. V-on 可以简写成什么？

8. Vue中可以遍历的指令是什么？

9. Vue里父子通信，父传子如何实现，具体步骤

10. Vue里父子通信，子传父如何实现，具体步骤

11. Vue指令的功能

12. Vue的双向数据绑定是由哪个模块实现，原理是是什么？具体步骤是什么？

# Spring+SpringBoot+Mybatis
1. SpringBoot 历史，框架的作用，为啥要学习框架
>2012 年 10 月，Mike Youngstrom 在 Spring jira 中创建了一个功能请求 ， 要求在 Spring 框架中支持无容器 Web 应用程序体系结构。他谈到了在主容器引导 spring 容器内配置 Web 容器服务。这是 jira 请求的摘录：我认为 Spring 的 Web 应用体系结构可以大大简化，如果它提供了从上到下利用 Spring 组件和配置模型的工具和参考体系结构。在简单的 main()方法引导的 Spring 容器内嵌入和统一这些常用Web 容器服务的配置。

>- 为什么要使用Spring Boot
>因为Spring SpringMVC 需要使用大量的配置文件(xml)，还需要配置各种对象，把使用的对象放入到Spring容器中才能使用对象，需要了解其他框架的配置规则
>SpringBoot不需要配置文件，常用的框架和第三方库已经配置好，可以直接使用
>开发效率高，使用方便

2. SSM 包含哪些内容
Spring+SpringBoot+Mybatis

3. SSM 如何配置

4. 如何创建项目 SpringBoot 的项目-(IDEA)里要包含 SpringMVC
    - 一种方式，创建Maven项目，在 pom.xml 依赖文件中手动加入(spring-boot-starter/spring-boot-starter-web/spring-webmvc) 依赖
    - 另一种方式，使用IDEA中Spring Initializr(Spring项目初始化器)，选择适当的依赖(Spring Web)进行项目初始化
    
5. 如何根据一个数据表创建实体类
将数据库表名转换成实体类对象名，表中属性转换成类对象中的属性

6. 掌握 Mybatis 的xml配置文件
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>

    <!--settings:控制mybatis全局行为-->
    <settings>
        <!--设置mybatis输出日志-->
        <setting name="logImpl" value="STDOUT_LOGGING"/>
    </settings>

    <!--环境配置：数据库的连接信息、
        dafault:必须和某人environment的id值一样。
        告诉mybatis使用哪个数据库的连接信息，也就是访问哪个数据库
    -->
    <environments default="mydev">
        <!--environment：一个数据库信息的配置，环境
            id:一个唯一值，自定义，表示环境名称
        -->
        <environment id="mydev">
            <!--
                transactionManager:mybatis的事务类型
                type:JDBC(表示使用jdbc中的Connection对象的commit，rollback)
            -->
            <transactionManager type="JDBC"/>
            <!--
                dataSource:表示数据源，连接数据库的
                type:表示数据源的类型，POOLED表示使用连接池
            -->
            <dataSource type="POOLED">
                <!--数据库的驱动类型名-->
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <!--连接数据库的url字符串-->
                <property name="url" value="jdbc:mysql://localhost:3306/****"/>
                <!--访问数据库的用户名-->
                <property name="username" value="****"/>
                <!--密码-->
                <property name="password" value="****"/>
            </dataSource>
        </environment>
    </environments>

    <!--sql mapper（sql映射文件）的位置-->
    <mappers>
        <!--一个mapper标签指定一个文件的位置
            从类路径开始的路径信息 target/clasess(类路径)
        -->
        <mapper resource="com/../*.xml"/>
    </mappers>
</configuration>

```
7. spring boot 的核心注解-@SpringBootApplication 包含哪些注解
@SpringBootApplication 【复合注解】  
由：
- @SpringBootConfiguration
- @EnableAutoConfiguration
- @ComponentScan


>1. @SpringBootConfiguration
>
```java
@Configuration
public @interface SpringBootConfiguration {
    @AliasFor(
            annotation = Configuration.class
    )
    boolean proxyBeanMethods() default true;
}
```
>说明：使用了 @SpringBootConfiguration 注解标注的类，可以作为配置文件使用（使用Bean声明对象，注入容器）

>2. @EnableAutoConfiguration  
>启动自动配置，把java对象配置后，注入到Spring容器中。（例如将mybatis对象创建好并注入容器）

>3. @ComponentScan  
>扫描器，找到注解，根据注解的功能完成创建对象、给属性赋值等操作  
>默认扫描包的位置：@ComponentScan所在的类的包以及子包