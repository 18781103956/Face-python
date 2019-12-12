/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : face_sign

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 09/09/2019 10:06:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `Work_account` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `rea_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pass_word` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Work_account`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('111', '11', '111');
INSERT INTO `account` VALUES ('6017200000', '张三', '123456789');
INSERT INTO `account` VALUES ('6017203235', '李德龙', 'zz15386621270');

-- ----------------------------
-- Table structure for class_table
-- ----------------------------
DROP TABLE IF EXISTS `class_table`;
CREATE TABLE `class_table`  (
  `class_no` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_sum` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `class_teacher` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`class_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class_table
-- ----------------------------
INSERT INTO `class_table` VALUES ('001', '58', '丁一');
INSERT INTO `class_table` VALUES ('003', '10', '张三');
INSERT INTO `class_table` VALUES ('004', '44', '赵四');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cno` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `c_class` int(11) NULL DEFAULT NULL,
  `c_teacher` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`cno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('test', 'Test', NULL, '李四');

-- ----------------------------
-- Table structure for sc
-- ----------------------------
DROP TABLE IF EXISTS `sc`;
CREATE TABLE `sc`  (
  `sno` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cno` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sc
-- ----------------------------
INSERT INTO `sc` VALUES ('', '');
INSERT INTO `sc` VALUES ('test_0', 'test');

-- ----------------------------
-- Table structure for sign_in
-- ----------------------------
DROP TABLE IF EXISTS `sign_in`;
CREATE TABLE `sign_in`  (
  `id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `similar` int(11) NOT NULL,
  `s_time` datetime(0) NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sign_in
-- ----------------------------
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-25 15:24:50');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-25 15:24:50');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-25 15:24:50');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-25 15:24:50');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-25 15:48:48');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-25 15:48:48');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-25 15:48:48');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-25 15:48:48');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-25 16:00:43');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-25 16:00:43');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-25 16:00:43');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-25 16:00:43');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-25 16:03:37');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-25 16:03:37');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-25 16:03:37');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-25 16:03:37');
INSERT INTO `sign_in` VALUES ('test_0', 10, '2019-08-25 17:26:51');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-25 19:09:31');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-25 19:09:31');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-25 19:09:31');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-25 19:09:31');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-26 14:24:03');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-26 14:24:03');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-26 14:24:03');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-26 14:24:03');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-26 14:25:44');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-26 14:25:44');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-26 14:25:44');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-26 14:25:44');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-26 14:32:06');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-26 14:32:06');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-26 14:32:06');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-26 14:32:06');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-26 18:52:17');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-26 18:52:17');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-26 18:52:17');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-26 18:52:17');
INSERT INTO `sign_in` VALUES ('test_1', 100, '2019-08-27 08:56:44');
INSERT INTO `sign_in` VALUES ('test_3', 100, '2019-08-27 08:56:44');
INSERT INTO `sign_in` VALUES ('test_2', 44, '2019-08-27 08:56:44');
INSERT INTO `sign_in` VALUES ('test_2', 100, '2019-08-27 08:56:44');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stu_id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stu_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stu_sex` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stu_class` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sign_val` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('2020001', '李永乐', '男', '001', '0');
INSERT INTO `student` VALUES ('2020002', '女一', '女', '001', '96');
INSERT INTO `student` VALUES ('2020003', '男一', '男', '001', '100');
INSERT INTO `student` VALUES ('2020004', '男二', '男', '001', '97');

SET FOREIGN_KEY_CHECKS = 1;
