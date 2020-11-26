import Database_Controller.repository as repository
import Database_Controller.models.info_table_model as models
import json


def get_bot_info():
    info_bot_entity = repository.get_latest_version()
    print("internal_services.get_bot_info -> versão buscada no banco")
    progbois = models.info_dev([models.dev(**brother) for brother in json.loads(info_bot_entity[3])])

    return("Você está curtindo nosso Rito-Bot, criado por: " + names_to_formatted_string(progbois.devs) + ".\n\n" +
           "Atualmente estamos na versão: " + version_and_comment(info_bot_entity[1]) + "\n" +
           "Contamos com um total de " + formatted_num_users(info_bot_entity[2]))


def get_version_details(version):
    info_bot_details = repository.get_version_details(str(version))
    print("internar_services.get_version_details -> retorno do banco: " + str(info_bot_details))
    if info_bot_details is None:
        return "Bip bip, versão não encontrada.\nMe progamaram errado? ( ; ω ; )"
    return("Versão: " + info_bot_details[0] + "\n" +
           "Lançada em: " + info_bot_details[1].strftime("%m/%d/%y") + "\n" +
           "Detalhes: \n\t" + str(info_bot_details[2])).replace("|", "\n\t")


def names_to_formatted_string(devs):
    except_last = ", ".join([dev.nome for dev in devs[:-1]])
    return except_last + " e " + devs[-1].nome


def version_and_comment(version):
    if float(version) < 0.5:
        return version + " (essa versão ainda é alfa... você só pode ser um tester) (:౦ ‸ ౦:)"
    if float(version) < 1.0:
        return version + " (essa é a versão beta, logo logo nosso bot estará lançado!)"


def formatted_num_users(num_users):
    if num_users == 0:
        return str(num_users) + " usuários..."
    return num_users + " usuários... (─‿‿─)♡"
