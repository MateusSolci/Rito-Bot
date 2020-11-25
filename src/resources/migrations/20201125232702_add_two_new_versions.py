# -*- coding: utf-8 -*-


# Uncomment should_run if this is a repeat migration
# def should_run(cursor):
#     # TODO return True if migration should run


def up(cursor):
    cursor.execute("""
    INSERT INTO public.tabela_info(data_versao, versao, quantidade_usuarios, info_time_dev, detalhes_versao) VALUES
    ('2020-11-22', '0.9', 0, '[{"nome": "Giacomo Magri"}, {"nome": "Lucas Valente"}, {"nome": "Mateus Solci"}]', 'implementada a página de consulta na web|os comandos ficaram mais bonitos'),
    ('2020-11-25', '1.0', 0, '[{"nome": "Giacomo Magri"}, {"nome": "Lucas Valente"}, {"nome": "Mateus Solci"}]', 'finalmente estamos on 24/7!')
    """)
    # if a super user database connection is needed
    # from dbmigrator import super_user
    # with super_user() as super_cursor:
    #     pass


def down(cursor):
    cursor.execute("""
    DELETE FROM public.tabela_info WHERE versao = 0.9 OR versao = 1.0
    """)
    pass
