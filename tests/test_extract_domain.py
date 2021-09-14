# import json
import logging
import os

from smalldoc import parse

logger = logging.getLogger(__name__)

WORKING_DIR = f'{os.path.dirname(__file__)}/data'
MODULE_NAME = 'fakemodule'
NB_STATIC_FUNCTION_EXPECTED = 6


def test_extract_module_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert_dict_contain(
        {
            'name': 'fakemodule',
            'description': 'A fake module ot our tests'
        },
        result
        ,
        'module domain'
    )


def test_should_extract_small_class_static_function_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'functions' in result
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    assert result['functions'][0]['name'] == 'a_static_function'
    assert result['functions'][0]['parameters'] == [
        {
            'name': 'a_parameter',
            'type': '',
            'doc': 'A small param'
        }
    ]


def test_should_extract_small_class_static_typed_function_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'functions' in result
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    assert result['functions'][1]['name'] == 'a_static_function_typed'
    assert result['functions'][1]['parameters'] == [
        {
            'name': 'a_parameter',
            'type': 'int',
            'doc': 'int typed parameter'
        }
    ]


def test_should_extract_small_class_static_function_return_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    logger.debug(result['functions'][2])
    assert result['functions'][2]['return'] == {
        'type': 'int',
        'doc': 'A value'
    }


def test_should_extract_small_class_static_function_return_typed_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    logger.debug(result['functions'][3])
    assert result['functions'][3]['return'] == {
        'type': 'int',
        'doc': ''
    }
    assert result['functions'][3]['def'] == 'def a_static_function_which_return_type(a_parameter) -> int'


def test_should_extract_small_class_static_function_whit_args_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'functions' in result
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    assert result['functions'][4]['name'] == 'a_static_function_with_args'
    assert result['functions'][4]['parameters'] == [
        {
            'name': '*args',
            'type': '',
            'doc': ''
        }
    ]


def test_should_extract_small_class_static_function_whit_kwargs_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'functions' in result
    assert len(result['functions']) == NB_STATIC_FUNCTION_EXPECTED
    assert result['functions'][5]['name'] == 'a_static_function_with_kwargs'
    assert result['functions'][5]['parameters'] == [
        {
            'name': '**kwargs',
            'type': '',
            'doc': ''
        }
    ]


def test_should_extract_small_class_static_function_with_def():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert result['functions'][0]['name'] == 'a_static_function'
    assert 'def' in result['functions'][0]
    assert result['functions'][0]['def'] == 'def a_static_function(a_parameter)'


def test_should_extract_small_class():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'classes' in result
    assert len(result['classes']) == 1
    assert result['classes'][0]['name'] == 'ASmallClass'
    assert result['classes'][0]['doc'] == 'A small class'
    assert 'functions' in result['classes'][0]
    assert len(result['classes'][0]['functions']) == 3
    # logger.debug(json.dumps(result, indent=2))


def test_extract_sub_module_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'modules' in result
    assert len(result['modules']) == 1


def test_extract_nested_classes_doc():
    # Given

    # When
    result = parse(WORKING_DIR, MODULE_NAME)

    # Then
    assert 'modules' in result
    assert len(result['modules']) == 1
    assert 'classes' in result['modules'][0]['classes'][0]
    logger.debug(result['modules'][0]['classes'][0]['classes'])
    assert len(result['modules'][0]['classes'][0]['classes']) == 1


def assert_dict_contain(expected: dict, result: dict, dict_name: str = 'dict'):
    assert expected.items() <= result.items(), f'Expected {dict_name} not match expected: {expected.items() - result.items()}'
