import Database_Controller.repository as repository
import Database_Controller.models.info_table_model as models
import json

def get_bot_info():
    info_bot_entity = repository.get_latest_version()
    progbois = models.info_dev([models.dev(**brother) for brother in json.loads(info_bot_entity[3])])
    
    return("Você tá curtindo nosso Rito-Bot, criado pelos gatão: " + names_to_formatted_string(progbois.devs) + "\n" +
        "Atualmente estamos na versão: " + version_and_comment(info_bot_entity[1]) + "\n" +
        "Contamos com um total de: " + formatted_num_users(info_bot_entity[2])
    )


def names_to_formatted_string(devs):
    except_last = ", ".join([dev.nome for dev in devs[:-1]]) 
    return except_last + " e " + devs[-1].nome


def version_and_comment(version):
    if (float(version) < 0.5): return version + " (essa versão ainda é alfa... você só pode ser um tester)"
    if (float(version) < 1.0): return version + " (essa é a versão beta, logo logo nosso bot tá lançado!)"
    return version + " (para mais detalhes dessa versão use o comando -versao <versao>)"


def formatted_num_users(num_users):
    if (num_users == 0): return str(num_users) + " usuários... (╥﹏╥)"
    return num_users + " usuários... (─‿‿─)♡"