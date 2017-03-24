


create table productos(

id_producto tinyint(2) not null auto_increment primary key,

producto varchar(30) not null,

descripcion varchar(35) not null,

existencias tinyint(3) not null,

precio_venta smallint(5) not null,

precio_compra smallint(5) not null

)
engine InnoDB;



insert into productos(producto, descripcion, existencias, precio_venta, precio_compra) values
('sdfs', 'sdfdsf', '69','20','35')
