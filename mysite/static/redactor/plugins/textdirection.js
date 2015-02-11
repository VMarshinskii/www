if (!RedactorPlugins) var RedactorPlugins = {};

(function($)
{
	RedactorPlugins.textdirection = function()
	{
		return {
			init: function()
			{
				var that = this;
				var dropdown = {};

				dropdown.ltr = { title: 'Слева направо', func: that.textdirection.setLtr };
				dropdown.rtl = { title: 'Справа налево', func: that.textdirection.setRtl};

				var button = this.button.add('textdirection', 'Обтекание текста');
				this.button.addDropdown(button, dropdown);
			},
			setRtl: function()
			{
				this.buffer.set();
				this.block.setAttr('dir', 'rtl');
			},
			setLtr: function()
			{
				this.buffer.set();
				this.block.removeAttr('dir');
			}
		};
	};
})(jQuery);
