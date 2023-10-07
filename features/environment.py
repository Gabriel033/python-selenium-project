import os

from settings.conf import driver_options


def before_all(context):
    carpeta = "./reports"
    # Verifica si la carpeta existe
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        # Obtén una lista de todos los elementos en la carpeta
        elementos = os.listdir(carpeta)

        # Recorre la lista de elementos y elimina cada uno
        for elemento in elementos:
            elemento_ruta = os.path.join(carpeta, elemento)

            # Verifica si es un archivo y lo elimina
            if os.path.isfile(elemento_ruta):
                os.remove(elemento_ruta)
            # Si es una carpeta, puedes usar shutil para eliminarla de manera recursiva
            elif os.path.isdir(elemento_ruta):
                import shutil
                shutil.rmtree(elemento_ruta)
    else:
        pass
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, driver):
    context.driver = None
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, driver):
    if driver_options.EXECUTION_OPTIONS.get('close-driver', False):
        try:
            context.diver.close()
        except:
            pass
        context.driver.quit()
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass
