Blockly.Blocks['forward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("move forward");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['Right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("Turn"), "NAME")
        .appendField(new Blockly.FieldDropdown([["Right","Right "], ["Left","Left"]]), "Turn");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['Left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("Turn"), "NAME")
        .appendField(new Blockly.FieldDropdown([["Left","Left"], ["Right","Right "]]), "Turn");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['forward'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  //var code = "document.getElementById('circle').value = "Forward";"
  //return code;
  return 'Forward;\n';
};

Blockly.JavaScript['Right'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  //var code = block.getFieldValue('Turn');
  //var code = "document.getElementById('circle').value = "Forward";"
  //return code;
  //return 'Right(\'block_id_' + block.id + '\');\n';
  return 'Right;\n';
};

Blockly.JavaScript['Left'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  //var code = "document.getElementById('circle').value = "Forward";"
  //return code;
  return 'Left;\n';
};

