
CREATE table data_set.abon_cities
(
    id_abon VARCHAR(50) PRIMARY KEY,
    city varchar(255),
    FOREIGN KEY (city)  REFERENCES states (s_city),
    FOREIGN KEY (id_abon)  REFERENCES  subscriber_information (id_abon)
);
insert into data_set.states  (`s_city`,`state`) values ('Montgomery','Alabama');
insert into data_set.states  (`s_city`,`state`) values ('Juneau','Alaska');
insert into data_set.states  (`s_city`,`state`) values ('Phoenix','Arizona');
insert into data_set.states  (`s_city`,`state`) values ('Little Rock','Arkansas');
insert into data_set.states  (`s_city`,`state`) values ('Sacramento','California');
insert into data_set.states  (`s_city`,`state`) values ('Denver','Colorado');
insert into data_set.states  (`s_city`,`state`) values ('Hartford','Connecticut');
insert into data_set.states  (`s_city`,`state`) values ('Dover','Delaware');
insert into data_set.states  (`s_city`,`state`) values ('Tallahassee','Florida');
insert into data_set.states  (`s_city`,`state`) values ('Atlanta','Georgia');
insert into data_set.states  (`s_city`,`state`) values ('Honolulu','Hawaii');
insert into data_set.states  (`s_city`,`state`) values ('Boise','Idaho');
insert into data_set.states  (`s_city`,`state`) values ('Springfield','Illinois');
insert into data_set.states  (`s_city`,`state`) values ('Indianapolis','Indiana');
insert into data_set.states  (`s_city`,`state`) values ('Des Moines','Iowa');
insert into data_set.states  (`s_city`,`state`) values ('Topeka','Kansas');
insert into data_set.states  (`s_city`,`state`) values ('Frankfort','Kentucky');
insert into data_set.states  (`s_city`,`state`) values ('Baton Rouge','Louisiana');
insert into data_set.states  (`s_city`,`state`) values ('Augusta','Maine');
insert into data_set.states  (`s_city`,`state`) values ('Annapolis','Maryland');
insert into data_set.states  (`s_city`,`state`) values ('Boston','Massachusetts');
insert into data_set.states  (`s_city`,`state`) values ('Lansing','Michigan');
insert into data_set.states  (`s_city`,`state`) values ('Saint Paul','Minnesota');
insert into data_set.states  (`s_city`,`state`) values ('Jackson','Mississippi');
insert into data_set.states  (`s_city`,`state`) values ('Jefferson City','Missouri');
insert into data_set.states  (`s_city`,`state`) values ('Helena','Montana');
insert into data_set.states  (`s_city`,`state`) values ('Lincoln','Nebraska');
insert into data_set.states  (`s_city`,`state`) values ('Carson City','Nevada');
insert into data_set.states  (`s_city`,`state`) values ('Concord','New Hampshire');
insert into data_set.states  (`s_city`,`state`) values ('Trenton','New Jersey');
insert into data_set.states  (`s_city`,`state`) values ('Santa Fe','New Mexico');
insert into data_set.states  (`s_city`,`state`) values ('Albany','New York');
insert into data_set.states  (`s_city`,`state`) values ('Raleigh','North Carolina');
insert into data_set.states  (`s_city`,`state`) values ('Bismarck','North Dakota');
insert into data_set.states  (`s_city`,`state`) values ('Columbus','Ohio');
insert into data_set.states  (`s_city`,`state`) values ('Oklahoma City','Oklahoma');
insert into data_set.states  (`s_city`,`state`) values ('Salem','Oregon');
insert into data_set.states  (`s_city`,`state`) values ('Harrisburg','Pennsylvania');
insert into data_set.states  (`s_city`,`state`) values ('Providence','Rhode Island');
insert into data_set.states  (`s_city`,`state`) values ('Columbia','South Carolina');
insert into data_set.states  (`s_city`,`state`) values ('Pierre','South Dakota');
insert into data_set.states  (`s_city`,`state`) values ('Nashville','Tennessee');
insert into data_set.states  (`s_city`,`state`) values ('Austin','Texas');
insert into data_set.states  (`s_city`,`state`) values ('Salt Lake City','Utah');
insert into data_set.states  (`s_city`,`state`) values ('Montpelier','Vermont');
insert into data_set.states  (`s_city`,`state`) values ('Richmond','Virginia');
insert into data_set.states  (`s_city`,`state`) values ('Olympia','Washington');
insert into data_set.states  (`s_city`,`state`) values ('Charleston','West Virginia');
insert into data_set.states  (`s_city`,`state`) values ('Madison','Wisconsin');
insert into data_set.states  (`s_city`,`state`) values ('Cheyenne','Wyoming');



insert into data_set.abon_cities  (`id_abon`,`city`) values ('fdf40c5f-50d4-4d9f-a015-b5aece2aa944','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('d8e7f123-18f6-4c09-a683-d466ee1217e1','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c069c890-e499-4593-99ec-163aaedbaa90','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('acbfe937-0329-4ff6-9680-cbe1b866c8d1','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('3f8af854-26a1-449d-a4a7-9bcd06a17088','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('cf177d81-063b-4822-84ee-ceb5f726eb1e','Montgomery');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('6f6a0228-ad56-4b16-ba7d-6af91f0685da','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('20d4dd16-9a85-4e9b-895e-61b4e3e1390d','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c94977f8-fe0f-4d64-a3bf-29936bc015f8','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('93278b7e-c957-4ce4-9326-639e14594655','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('d511f782-3d04-4622-90f4-02eb8a7c6694','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('ccb53bc6-23e4-41be-b548-4694a7d31494','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('083aa6ce-0702-4521-9815-304e61894018','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('7e84e22a-15da-46dd-88f9-b095425d0c5e','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('0318507c-12d9-4d78-9224-77b82afadad9','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('6e15b129-d4e0-41a7-a3c4-32ea6a4a9623','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('a32c6a3f-2a65-4337-9b5c-0795d0f634e6','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f236b1d9-3cfd-4879-bf3c-dec6910cf8e0','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c49f41b1-2675-4cf0-837f-460256d2d25a','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('61518eff-0af4-459e-81ab-0ed58916ab75','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('e2783c9c-176e-4ab0-872c-ca266eb22bf8','Columbus');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('011379f1-910f-43cf-8600-a404594c32e5','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('78de8503-4c05-4756-b574-59f7f6c9d214','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('fe863776-81c9-45c2-b537-3b55ff176cdc','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('35d1dbd0-a3f6-4312-bb34-40772a652efc','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('181acbb2-0ebb-46d1-9374-a7d967bd4fae','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('28abe939-e728-4ef7-a0b3-7ab764514906','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('504c2e9b-1d7e-4363-9798-bc3d6d2e816c','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('5826ec5e-e6ba-4562-b261-4603b9ef9c06','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('706a44d5-f4fc-4991-961d-4085c6236478','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f07c6f72-4160-46a8-b75c-ca334dd26ab0','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('403ada69-ac9f-484b-a889-3bfe829d9391','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('ed95f5eb-bbf3-4271-825d-d5046c9058a6','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f2cb921f-165e-4b93-b8d1-a9d65cd42427','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('bfcd9f6a-9269-49f0-91b8-6a344e96a580','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('da2b4ec0-5d0e-48d6-950f-5281c64fb602','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('5db1732d-413e-4d46-b5c7-d4bf610d37f3','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c5f4f7c8-66ca-4e41-96cc-81112d922a76','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('a3fafec8-d796-42f1-9042-40007bbc1c9d','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('3b104f89-0f1c-4a4e-a0e8-479397678f2f','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f1f44b1c-31a6-46d2-8d88-b08a8152751f','Madison');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('3c23cefd-0b80-4341-9dd3-091c0c2d5f4f','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('0bd3137f-9569-4c25-b517-74ff9e77d0cb','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('553623b2-dfb2-49c2-8d59-e3a8ddd590f1','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('cbaf8a65-7d4c-4f9c-9cc8-f537bb4c9b2a','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('dd690375-cc17-4397-ae1a-e2edd7b6152d','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('4d731348-e17c-4eba-9994-879b77bd0b24','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f5fb6c2a-f496-43ee-b7a0-fb00b7220fd5','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('caec554f-64e6-42f9-bbdc-0b7db57dcefe','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('cbb50e0f-2f19-46e5-a5e1-5c6273e3255c','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('264d3cbf-4844-4806-a460-2207cfcffca1','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('2745f0b6-8135-4883-9a14-7e037e7ee66d','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('87fd5cc7-cc89-4351-a93c-84d7a2954d17','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('b2042fff-1b43-4525-9330-a158b903c43d','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('a46580b6-2500-44e9-98d2-a3f13d99b864','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('3938cbe2-6959-46cf-8143-b07dd7effed6','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('ce221149-b382-4b58-b530-37381dba4f5a','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('be76e1a3-4050-4934-9625-2d0a8a44bbee','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('b56d6e64-4bf7-4fc7-8fe6-657a96fc6a37','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('0d766150-3581-445c-beb4-463a7803add3','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('4cceead4-e82e-41d2-88a1-043af5ad6228','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('109a829b-fedd-4612-b354-effbe10d0be6','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('6502f3e7-9078-4492-96e8-9bb867cd2e82','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('4b2f5478-35cc-46ce-ae07-99b44dd8fe4e','Boston');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('abcab16b-baa2-4106-bf98-df1c6a1f9490','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('4b4d4195-3664-4573-be05-88cf9c793224','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('7dc19a0a-4548-40c9-9903-27d8f5826778','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('e32d708a-357e-42a6-8666-fc8cb6de0a6a','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('d2c3433c-e57e-4b22-9c1b-0c0f83477d9e','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('f2bcb9b0-4c11-4f02-9ea5-6bf1497465e3','Trenton');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('a6875f37-8979-4eab-93ff-3dfb08aff8c6','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('662d2a18-2281-46fa-9529-f3173a0c43f3','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('81e22e66-267d-4a8c-8aac-bc24e0779769','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('2bbddb65-e4f2-48a7-a99f-80499f035d8a','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('13392431-b388-4e7e-9095-b023a2e75cc6','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('5c1ca460-68f4-43ab-b66d-dc3f56dab683','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('bce9e6a2-f3c7-4b99-aed3-ee3ebd43cd22','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('6bbc7755-ade9-4fe3-a0f6-9c94d11a8201','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('1325a479-7b17-4267-af0a-ba7c1a56213c','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('395b2096-8e2c-4a74-9616-a0c9831c0e93','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('97200e6c-ff6c-4d6c-8e1d-65e6e972c629','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('77455b95-585b-4e3b-bb60-9d0cae5bc747','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('bc697da5-01bf-4aad-afa6-a484166656af','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('ada42e3d-294e-4b0b-bde3-d8136877956d','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c8212f2f-74da-47f7-9577-c140818259af','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('27f691bc-ba81-490a-b077-6c038f9652d9','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('e532f686-214b-4bf2-ad8a-3d46af8ae4b6','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('a5abfa61-2c19-43e0-97c8-112a35f2a40f','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('bd421219-ef2e-4ea1-983e-76a94d8abdf5','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('7f7164fa-f4a4-4b50-b7ae-36f92b4fba1a','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('966557f1-b688-4f2d-be19-46808ae4a768','Santa Fe');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('eece6b9c-2d39-49d3-8f30-eed492640c1b','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('c2f5c53d-2026-41c9-bcaa-bba46ce8c4f5','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('2b343f21-5445-4419-9ea8-14db9ccda1e2','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('b4f7ef94-0e62-4ca3-a0bf-2aac5e1bdbc2','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('18495a7b-a750-4068-8413-d1e6a67889a3','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('964c1902-e1db-440e-99da-ca36c4806b33','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('4ef47e0b-6751-4462-8883-5984a98a5370','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('dede7ffa-d32e-4efd-a789-8d89d75348cd','Nashville');
insert into data_set.abon_cities  (`id_abon`,`city`) values ('bf97da52-38c9-4a36-b147-7fe336c35c66','Nashville');


