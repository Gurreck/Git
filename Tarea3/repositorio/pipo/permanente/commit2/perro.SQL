/*
Created: 30/04/2021
Modified: 04/05/2021
Model: Oracle 11g Release 2
Database: Oracle 11g Release 2
*/


-- Create tables section -------------------------------------------------

-- Table UNA_tiposUsuarios

CREATE TABLE "UNA_tiposUsuarios"(
  "ID_tipoUsuario" Number NOT NULL,
  "Tip_nombre" NVarchar2(30) NOT NULL
)
/

-- Add keys for table UNA_tiposUsuarios

ALTER TABLE "UNA_tiposUsuarios" ADD CONSTRAINT "PK_UNA_tiposUsuarios" PRIMARY KEY ("ID_tipoUsuario")
/

-- Table UNA_usuarios

CREATE TABLE "UNA_usuarios"(
  "ID_usuario" Number NOT NULL,
  "Usu_nombre" NVarchar2(30) NOT NULL,
  "FK_tipoUsuario" Number NOT NULL
)
/

-- Create indexes for table UNA_usuarios

CREATE INDEX "IX_Relationship6" ON "UNA_usuarios" ("FK_tipoUsuario")
/

-- Add keys for table UNA_usuarios

ALTER TABLE "UNA_usuarios" ADD CONSTRAINT "PK_UNA_usuarios" PRIMARY KEY ("ID_usuario")
/

-- Table UNA_grupos

CREATE TABLE "UNA_grupos"(
  "ID_grupo" Number NOT NULL,
  "Gru_nombre" NVarchar2(30) NOT NULL,
  "Gru_puntaje" Integer,
  "FK_partida" Number NOT NULL
)
/

-- Create indexes for table UNA_grupos

CREATE INDEX "IX_Relationship9" ON "UNA_grupos" ("FK_partida")
/

-- Add keys for table UNA_grupos

ALTER TABLE "UNA_grupos" ADD CONSTRAINT "PK_UNA_grupos" PRIMARY KEY ("ID_grupo")
/

-- Table UNA_partidas

CREATE TABLE "UNA_partidas"(
  "ID_partida" Number NOT NULL,
  "Par_Nombre" NVarchar2(30) NOT NULL,
  "Par_estado" NVarchar2(10) NOT NULL,
  "Par_comienzo" Date,
  "Par_final" Date,
  "FK_usuario" Number NOT NULL,
  CONSTRAINT "Par_estado_check" CHECK (Par_estado in('Activa','Inactiva'))
)
/

-- Create indexes for table UNA_partidas

CREATE INDEX "IX_Relationship10" ON "UNA_partidas" ("FK_usuario")
/

-- Add keys for table UNA_partidas

ALTER TABLE "UNA_partidas" ADD CONSTRAINT "PK_UNA_partidas" PRIMARY KEY ("ID_partida")
/

-- Table UNA_preguntas

CREATE TABLE "UNA_preguntas"(
  "ID_pregunta" Number NOT NULL,
  "Pre_pregunta" NVarchar2(100) NOT NULL,
  "Pre_imagen" NVarchar2(50),
  "FK_partida" Number NOT NULL
)
/

-- Create indexes for table UNA_preguntas

CREATE INDEX "IX_Relationship12" ON "UNA_preguntas" ("FK_partida")
/

-- Add keys for table UNA_preguntas

ALTER TABLE "UNA_preguntas" ADD CONSTRAINT "PK_UNA_preguntas" PRIMARY KEY ("ID_pregunta")
/

-- Table UNA_dificultades

CREATE TABLE "UNA_dificultades"(
  "ID_dificultad" Number NOT NULL,
  "Dif_nivel" NVarchar2(10) NOT NULL
)
/

-- Add keys for table UNA_dificultades

ALTER TABLE "UNA_dificultades" ADD CONSTRAINT "PK_UNA_dificultades" PRIMARY KEY ("ID_dificultad")
/

-- Table UNA_permisos

CREATE TABLE "UNA_permisos"(
  "ID_permiso" Number NOT NULL,
  "Per_descripcion" NVarchar2(50) NOT NULL
)
/

-- Add keys for table UNA_permisos

ALTER TABLE "UNA_permisos" ADD CONSTRAINT "PK_UNA_permisos" PRIMARY KEY ("ID_permiso")
/

-- Table UNA_respuestas

CREATE TABLE "UNA_respuestas"(
  "ID_respuesta" Number NOT NULL,
  "Res_respuesta" NVarchar2(100) NOT NULL,
  "Res_estado" NVarchar2(10) NOT NULL
        CONSTRAINT "Res_estado_check" CHECK (Res_estado in('Correcta','Incorrecta')),
  "FK_pregunta" Number NOT NULL
)
/

-- Create indexes for table UNA_respuestas

CREATE INDEX "IX_Relationship13" ON "UNA_respuestas" ("FK_pregunta")
/

-- Add keys for table UNA_respuestas

ALTER TABLE "UNA_respuestas" ADD CONSTRAINT "PK_UNA_respuestas" PRIMARY KEY ("ID_respuesta")
/

-- Table UNA_permisos_tiposUsuarios

CREATE TABLE "UNA_permisos_tiposUsuarios"(
  "ID_permiso_tipoUsuario" Number NOT NULL,
  "FK_permiso" Number NOT NULL,
  "FK_tipoUsuario" Number NOT NULL
)
/

-- Create indexes for table UNA_permisos_tiposUsuarios

CREATE INDEX "IX_Relationship7" ON "UNA_permisos_tiposUsuarios" ("FK_tipoUsuario")
/

CREATE INDEX "IX_Relationship8" ON "UNA_permisos_tiposUsuarios" ("FK_permiso")
/

-- Add keys for table UNA_permisos_tiposUsuarios

ALTER TABLE "UNA_permisos_tiposUsuarios" ADD CONSTRAINT "PK_UNA_permisos_tiposUsuarios" PRIMARY KEY ("ID_permiso_tipoUsuario")
/

-- Table UNA_grupos_usuarios

CREATE TABLE "UNA_grupos_usuarios"(
  "ID_grupo_usuario" Number NOT NULL,
  "FK_grupo" Number NOT NULL,
  "FK_usuario" Number NOT NULL
)
/

-- Create indexes for table UNA_grupos_usuarios

CREATE INDEX "IX_Relationship4" ON "UNA_grupos_usuarios" ("FK_grupo")
/

CREATE INDEX "IX_Relationship5" ON "UNA_grupos_usuarios" ("FK_usuario")
/

-- Add keys for table UNA_grupos_usuarios

ALTER TABLE "UNA_grupos_usuarios" ADD CONSTRAINT "PK_UNA_grupos_usuarios" PRIMARY KEY ("ID_grupo_usuario")
/

-- Table UNA_Parametros

CREATE TABLE "UNA_Parametros"(
  "ID_parametro" Number NOT NULL,
  "Par_Puntos" Integer NOT NULL,
  "Par_tiempoExpiracion" Integer,
  "Par_duplicaValor" NVarchar2(2) NOT NULL
        CONSTRAINT "Par_duplicaValor_check" CHECK (Par_duplicaValor in('Si','No')),
  "Par_eliminarTiempoExpiracion" NVarchar2(2) NOT NULL
        CONSTRAINT "Par_eliminarTiempo_check" CHECK (Par_eliminarTiempoExpiracion in('Si','No')),
  "Par_duplicaTiempoExpiracion" NVarchar2(2) NOT NULL
        CONSTRAINT "Par_duplicaTiempo_check" CHECK (Par_duplicaTiempoExpiracion in('Si','No')),
  "FK_pregunta" Number NOT NULL,
  "FK_dificultad" Number NOT NULL
)
/

-- Create indexes for table UNA_Parametros

CREATE INDEX "IX_Relationship15" ON "UNA_Parametros" ("FK_pregunta")
/

CREATE INDEX "IX_Relationship16" ON "UNA_Parametros" ("FK_dificultad")
/

-- Add keys for table UNA_Parametros

ALTER TABLE "UNA_Parametros" ADD CONSTRAINT "PK_UNA_Parametros" PRIMARY KEY ("ID_parametro")
/

-- Table UNA_bonificaciones

CREATE TABLE "UNA_bonificaciones"(
  "ID_bonificacion" Number NOT NULL,
  "Bon_descripcion" NVarchar2(50) NOT NULL
)
/

-- Add keys for table UNA_bonificaciones

ALTER TABLE "UNA_bonificaciones" ADD CONSTRAINT "PK_UNA_bonificaciones" PRIMARY KEY ("ID_bonificacion")
/

-- Table UNA_bonificaciones_grupos

CREATE TABLE "UNA_bonificaciones_grupos"(
  "ID_bonificacion_grupo" Number NOT NULL,
  "FK_bonificacion" Number NOT NULL,
  "FK_grupo" Number NOT NULL
)
/

-- Create indexes for table UNA_bonificaciones_grupos

CREATE INDEX "IX_Relationship3" ON "UNA_bonificaciones_grupos" ("FK_grupo")
/

CREATE INDEX "IX_Relationship2" ON "UNA_bonificaciones_grupos" ("FK_bonificacion")
/

-- Add keys for table UNA_bonificaciones_grupos

ALTER TABLE "UNA_bonificaciones_grupos" ADD CONSTRAINT "PK_UNA_bonificaciones_grupos" PRIMARY KEY ("ID_bonificacion_grupo")
/

-- Table UNA_accionesPremiadas

CREATE TABLE "UNA_accionesPremiadas"(
  "ID_accionPremiada" Number NOT NULL,
  "Acc_descripcion" NVarchar2(40) NOT NULL,
  "FK_bonificacion" Number NOT NULL
)
/

-- Create indexes for table UNA_accionesPremiadas

CREATE INDEX "IX_Relationship1" ON "UNA_accionesPremiadas" ("FK_bonificacion")
/

-- Add keys for table UNA_accionesPremiadas

ALTER TABLE "UNA_accionesPremiadas" ADD CONSTRAINT "PK_UNA_accionesPremiadas" PRIMARY KEY ("ID_accionPremiada")
/

-- Table UNA_resultados

CREATE TABLE "UNA_resultados"(
  "ID_resultado" Number NOT NULL,
  "FK_grupo_usuario" Number NOT NULL,
  "FK_respuesta" Number NOT NULL
)
/

-- Create indexes for table UNA_resultados

CREATE INDEX "IX_Relationship11" ON "UNA_resultados" ("FK_grupo_usuario")
/

CREATE INDEX "IX_Relationship14" ON "UNA_resultados" ("FK_respuesta")
/

-- Add keys for table UNA_resultados

ALTER TABLE "UNA_resultados" ADD CONSTRAINT "PK_UNA_resultados" PRIMARY KEY ("ID_resultado")
/




-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "UNA_permisos_tiposUsuarios" ADD CONSTRAINT "Relationship8" FOREIGN KEY ("FK_permiso") REFERENCES "UNA_permisos" ("ID_permiso")
/



ALTER TABLE "UNA_permisos_tiposUsuarios" ADD CONSTRAINT "Relationship7" FOREIGN KEY ("FK_tipoUsuario") REFERENCES "UNA_tiposUsuarios" ("ID_tipoUsuario")
/



ALTER TABLE "UNA_usuarios" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("FK_tipoUsuario") REFERENCES "UNA_tiposUsuarios" ("ID_tipoUsuario")
/



ALTER TABLE "UNA_Parametros" ADD CONSTRAINT "Relationship15" FOREIGN KEY ("FK_pregunta") REFERENCES "UNA_preguntas" ("ID_pregunta")
/



ALTER TABLE "UNA_grupos" ADD CONSTRAINT "Relationship9" FOREIGN KEY ("FK_partida") REFERENCES "UNA_partidas" ("ID_partida")
/



ALTER TABLE "UNA_Parametros" ADD CONSTRAINT "Relationship16" FOREIGN KEY ("FK_dificultad") REFERENCES "UNA_dificultades" ("ID_dificultad")
/



ALTER TABLE "UNA_accionesPremiadas" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("FK_bonificacion") REFERENCES "UNA_bonificaciones" ("ID_bonificacion")
/



ALTER TABLE "UNA_preguntas" ADD CONSTRAINT "Relationship12" FOREIGN KEY ("FK_partida") REFERENCES "UNA_partidas" ("ID_partida")
/



ALTER TABLE "UNA_respuestas" ADD CONSTRAINT "Relationship13" FOREIGN KEY ("FK_pregunta") REFERENCES "UNA_preguntas" ("ID_pregunta")
/



ALTER TABLE "UNA_resultados" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("FK_grupo_usuario") REFERENCES "UNA_grupos_usuarios" ("ID_grupo_usuario")
/



ALTER TABLE "UNA_resultados" ADD CONSTRAINT "Relationship14" FOREIGN KEY ("FK_respuesta") REFERENCES "UNA_respuestas" ("ID_respuesta")
/



ALTER TABLE "UNA_bonificaciones_grupos" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("FK_bonificacion") REFERENCES "UNA_bonificaciones" ("ID_bonificacion")
/



ALTER TABLE "UNA_bonificaciones_grupos" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("FK_grupo") REFERENCES "UNA_grupos" ("ID_grupo")
/



ALTER TABLE "UNA_grupos_usuarios" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("FK_grupo") REFERENCES "UNA_grupos" ("ID_grupo")
/



ALTER TABLE "UNA_grupos_usuarios" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("FK_usuario") REFERENCES "UNA_usuarios" ("ID_usuario")
/



ALTER TABLE "UNA_partidas" ADD CONSTRAINT "Relationship10" FOREIGN KEY ("FK_usuario") REFERENCES "UNA_usuarios" ("ID_usuario")
/




