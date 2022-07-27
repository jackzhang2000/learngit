/*
 Navicat Premium Data Transfer

 Source Server         : postgreSQL
 Source Server Type    : PostgreSQL
 Source Server Version : 110014
 Source Host           : localhost:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 110014
 File Encoding         : 65001

 Date: 15/03/2022 14:56:19
*/
-----

-- ----------------------------
-- Table structure for myadmin_dataset
-- ----------------------------
DROP TABLE IF EXISTS "public"."myadmin_dataset";
CREATE TABLE "public"."myadmin_dataset" (
  "ID" SERIAL PRIMARY KEY,
    "Dataset_Name" text COLLATE "pg_catalog"."default" NOT NULL,
  "Num_Of_Files" int4 NOT NULL,
  "Num_Of_Annotated_Events" int4 NOT NULL,
  "Species_identified" text COLLATE "pg_catalog"."default",
  "Sampling_rate" varchar(100) COLLATE "pg_catalog"."default",
  "Total_Duration" varchar(100) COLLATE "pg_catalog"."default",
  "Total_Size" varchar(100) COLLATE "pg_catalog"."default",
  "Number_of_Subsets" int4,
  "Location" varchar(100) COLLATE "pg_catalog"."default",
  "Latitude" varchar(50) COLLATE "pg_catalog"."default",
  "Longitude" varchar(50) COLLATE "pg_catalog"."default",
  "Depth" varchar(100) COLLATE "pg_catalog"."default",
  "YAML_Filename" text COLLATE "pg_catalog"."default",
  "Summary_by_Species" varchar(100) COLLATE "pg_catalog"."default",
  "Summary_by_Ecotypes" varchar(100) COLLATE "pg_catalog"."default",
  "Summary_by_Pods" varchar(100) COLLATE "pg_catalog"."default",
  "Summary_by_CallType" varchar(100) COLLATE "pg_catalog"."default",
  "create_at" timestamptz(6) NOT NULL,
  "update_at" timestamptz(6) NOT NULL,
  "create_by" varchar(50) COLLATE "pg_catalog"."default",
  "update_by" varchar(50) COLLATE "pg_catalog"."default",
  "Annotation_type" int4,
  "File_Size" varchar(100) COLLATE "pg_catalog"."default",
  "record_start" timestamptz(6),
  "record_end" timestamptz(6),
  "Ecotype" varchar(512) COLLATE "pg_catalog"."default",
  "Pods" varchar(255) COLLATE "pg_catalog"."default",
  "Calltype" varchar(255) COLLATE "pg_catalog"."default"
)
;

ALTER TABLE "public"."myadmin_dataset" 
  OWNER TO "postgres";

-- ----------------------------
-- Records of myadmin_dataset
-- ----------------------------
INSERT INTO "public"."myadmin_dataset" VALUES (1, 'Jasco_Roberts_Bank', 50, 2078, 'Killer Whale', '44.1 kHz', '2886', '1.8GB', 5, 'Roberts Point, British Columbia, Canada', '49.07', '123.18', 20.6, 'Roberts_bank.yml', 'test', 'test', 'test', 'test', '2022-02-22 14:47:16-04', '2022-02-22 14:47:20-04', 'Jack', 'Jack');
INSERT INTO "public"."myadmin_dataset" VALUES (2, 'jasco_boundary_pass', 100, 2078, 'Killer Whale', '96 kHz', '2886', '2.1GB', 5, 'Roberts Point, British Columbia, Canada', '49.07', '123.18', 20.6, 'Roberts_bank.yml', 'test', 'test', 'test', 'test', '2022-02-24 14:47:16-04', '2022-02-14 14:47:20-04', 'Jack', 'Jack');

ALTER SEQUENCE myadmin_dataset_ID_seq RESTART WITH 3; 

CREATE TABLE "public"."myadmin_datasetdetail" (
  "ID" SERIAL PRIMARY KEY,
  "Dataset_ID" int4 NOT NULL,
  "File_type" varchar(50) COLLATE "pg_catalog"."default",
  "File_name" text COLLATE "pg_catalog"."default",
  "Download_link" text COLLATE "pg_catalog"."default",
  "create_at" timestamptz(6),
  "update_at" timestamptz(6),
  "create_by" varchar(50) COLLATE "pg_catalog"."default",
  "update_by" varchar(50) COLLATE "pg_catalog"."default"
)
;

INSERT INTO "myadmin_datasetdetail"("ID", "Dataset_ID", "File_type", "File_name", "Download_link", "create_at", "update_at", "create_by", "update_by") VALUES (1, 9, 'zip', 'Roberts_Bank001.zip', 'http://halo.dal.ca/data/Roberts_Bank001.zip', '2022-02-24 11:40:05-04', '2022-02-24 11:40:08-04', 'Jack', 'Jack');


ALTER SEQUENCE myadmin_datasetdetail_ID_seq RESTART WITH 2;
	
drop table myadmin_annotation;
CREATE TABLE "public"."myadmin_annotation" (
  "ID" SERIAL PRIMARY KEY,
  "Dataset_ID" int4 NOT NULL,
  "Annotation_type" int4 NOT NULL DEFAULT 1,
  "File_name" text COLLATE "pg_catalog"."default",
  "Create_at" timestamptz(6),
  "Update_at" timestamptz(6),
  "Create_by" varchar(50) COLLATE "pg_catalog"."default",
  "Update_by" text COLLATE "pg_catalog"."default",
  "Dataset_name" varchar(100) COLLATE "pg_catalog"."default",
  "File_path" varchar(255) COLLATE "pg_catalog"."default"
)
;

INSERT INTO "myadmin_annotation"("ID", "Dataset_ID", "Annotation_type", "File_name", "Start", "End", "Freq_min", "Freq_max", "Sound_id_species", "Ecotype", "Pod", "Call_type", "Comments", "Duration", "Create_at", "Update_at", "Create_by", "Update_by") VALUES (1, 9, 'Detailed', 'JASCOAMARHYDROPHONEC000682_20171103T150328.359Z.wav', 52.1, 54.6, 1588.4, 2322.5, 'KW', 'KWSR', 'J', 'S1', '', 1.44, '2022-02-24 11:30:58-04', '2022-02-24 11:31:00-04', 'Jack', 'Jack');
INSERT INTO "myadmin_annotation"("ID", "Dataset_ID", "Annotation_type", "File_name", "Start", "End", "Freq_min", "Freq_max", "Sound_id_species", "Ecotype", "Pod", "Call_type", "Comments", "Duration", "Create_at", "Update_at", "Create_by", "Update_by") VALUES (2, 9, 'Detailed', 'JASCOAMARHYDROPHONEC000682_20171103T150328.359Z.wav', 78.613, 79.4504381, 1444, 2960.3, 'Vessel Noise', NULL, NULL, NULL, 'Engine noise', 1.65024566, '2022-02-24 11:43:12-04', '2022-02-24 11:43:16-04', 'Jack', 'Jack');
INSERT INTO "myadmin_annotation"("ID", "Dataset_ID", "Annotation_type", "File_name", "Start", "End", "Freq_min", "Freq_max", "Sound_id_species", "Ecotype", "Pod", "Call_type", "Comments", "Duration", "Create_at", "Update_at", "Create_by", "Update_by") VALUES (3, 9, 'Detailed', 'JASCOAMARHYDROPHONEC000682_20171103T150328.359Z.wav', 52.1, 54.6, 1588.4, 2322.5, 'KW', 'KWSR', 'J', 'S1', '', 1.44, '2022-02-24 11:30:58-04', '2022-02-24 11:31:00-04', 'Jack', 'Jack');
INSERT INTO "myadmin_annotation"("ID", "Dataset_ID", "Annotation_type", "File_name", "Start", "End", "Freq_min", "Freq_max", "Sound_id_species", "Ecotype", "Pod", "Call_type", "Comments", "Duration", "Create_at", "Update_at", "Create_by", "Update_by") VALUES (4, 9, 'Detailed', 'JASCOAMARHYDROPHONEC000682_20171103T150328.359Z.wav', 78.613, 79.4504381, 1444, 2960.3, 'Vessel Noise', NULL, NULL, NULL, 'Engine noise', 1.65024566, '2022-02-24 11:43:12-04', '2022-02-24 11:43:16-04', 'Jack', 'Jack');

ALTER SEQUENCE myadmin_annotation_ID_seq RESTART WITH 5;

CREATE TABLE "public"."myadmin_model" (
  "ID" SERIAL PRIMARY KEY,
  "Model_Name" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "Dataset_ID" int4 NOT NULL,
  "Download_link" text COLLATE "pg_catalog"."default" NOT NULL,
  "Model_Level" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "Model_details" text COLLATE "pg_catalog"."default" NOT NULL,
  "Architecture" text COLLATE "pg_catalog"."default" NOT NULL,
  "Training_Set" text COLLATE "pg_catalog"."default" NOT NULL,
  "Input_processing" text COLLATE "pg_catalog"."default" NOT NULL,
  "Input_Duration" text COLLATE "pg_catalog"."default" NOT NULL,
  "Flow_chart" text COLLATE "pg_catalog"."default" NOT NULL,
  "Performance_Matric1" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "Performance_Matric2" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "Performance_Matric3" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "Performance_Matric4" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "Create_at" timestamptz(6) NOT NULL,
  "Update_at" timestamptz(6) NOT NULL,
  "Create_by" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "Update_by" varchar(50) COLLATE "pg_catalog"."default" NOT NULL)
;

CREATE TABLE "public"."shop" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "cover_pic" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "banner_pic" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "address" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "phone" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "status" int4 NOT NULL DEFAULT 1,
  "create_at" timestamptz(6) DEFAULT NULL::timestamp with time zone,
  "update_at" timestamptz(6) DEFAULT NULL::timestamp with time zone
)
;

insert  into shop values 
(1,'田老师红烧肉-朝阳将台路店','12341234.jpg','lg.jpg','北京市朝阳区将台乡东八间房村西临8号','12345678905',1,'2020-07-20 10:12:34','2020-07-24 12:34:56'),
(2,'田老师红烧肉-海淀区上地店','57892456.jpg','lg.jpg','北京市海定区上地三街嘉华大厦A座10号','13456789209',1,'2020-07-21 12:23:45','2020-07-22 20:42:16'),
(3,'田老师红烧肉-西城玉渊潭店','23454567.jpg','lg.jpg','北京市宣武区玉渊潭南路东123号','12345677654',2,'2020-07-24 08:20:32','2020-07-25 06:06:07');

ALTER SEQUENCE serial RESTART WITH 4;

CREATE TABLE "public"."product" (
  "id" SERIAL PRIMARY KEY,
  "shop_id" int8,
  "category_id" int8,
  "cover_pic" varchar(50) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "name" varchar(50) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "price" float8,
  "status" int4,
  "create_at" timestamptz(6) DEFAULT NULL::timestamp with time zone,
  "update_at" timestamptz(6) DEFAULT NULL::timestamp with time zone
  )
;

INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (1, 1, 1, '1536657620.5485704.jpg', '红烧肉+狮子头+饮料', 25, 1, '2020-07-11 09:20:20-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (2, 1, 1, '1536658352.9341557.jpg', '红烧肉+番茄鸡蛋', 22, 1, '2020-07-11 09:32:32-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (3, 1, 1, '1536658415.6838002.jpg', '梅菜扣肉+番茄鸡蛋', 22, 1, '2020-07-11 09:33:35-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (4, 1, 1, '1536658574.2847373.jpg', '肥牛+番茄鸡蛋', 22, 1, '2020-07-11 09:36:14-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (5, 1, 2, '1536658659.0446993.jpg', '梅菜扣肉饭', 19, 1, '2020-07-11 09:37:39-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (6, 1, 2, '1536658824.3976505.jpg', '木须肉饭', 16, 1, '2020-07-11 09:40:24-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (7, 1, 2, '1536658863.6732855.jpg', '肥牛饭', 19, 1, '2020-07-11 09:41:03-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (8, 1, 2, '1536658960.3954134.jpg', '无骨咖喱鸡饭', 18, 1, '2020-07-11 09:42:40-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (9, 1, 3, '1536659114.0440235.jpg', '木须肉', 12, 1, '2020-07-11 09:44:25-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (10, 1, 3, '1536659065.7972637.jpg', '番茄鸡蛋', 4, 1, '2020-07-11 09:45:14-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (11, 1, 3, '1536659197.7231221.jpg', '青菜', 4, 1, '2020-07-11 09:46:37-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (12, 1, 3, '1536659253.8842716.jpg', '单份香辣笋干烧肉', 15, 1, '2020-07-11 09:47:33-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (13, 1, 4, '1536659311.8699493.jpg', '番茄蛋花汤', 4, 1, '2020-07-11 09:48:31-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (14, 1, 4, '1536659364.7892513.jpg', '王老吉', 6, 1, '2020-07-11 09:49:24-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (15, 1, 4, '1536659563.3897648.jpg', '果粒橙', 5, 1, '2020-07-11 09:52:43-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (16, 1, 4, '1536659605.5561771.jpg', '矿泉水', 3, 1, '2020-07-11 09:53:25-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (17, 1, 4, '1536659688.4856157.jpg', '乌梅汁', 4, 1, '2020-07-11 09:54:48-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (18, 2, 7, '1536659065.7972636.jpg', '番茄鸡蛋', 4, 1, '2020-07-04 06:17:18-03', '2020-07-25 10:20:30-03');
INSERT INTO "product"("id", "shop_id", "category_id", "cover_pic", "name", "price", "status", "create_at", "update_at") VALUES (19, 3, 10, '1536658666.8341557.jpg', '红烧肉+西红柿鸡蛋', 24, 1, '2020-07-06 08:46:28-03', '2020-07-25 07:34:07-03');

ALTER SEQUENCE product_id_seq RESTART WITH 20; 
