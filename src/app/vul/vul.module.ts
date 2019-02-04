import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TargetBlankDirective } from './target-blank.directive';

@NgModule({
  declarations: [TargetBlankDirective],
  exports: [TargetBlankDirective],
  imports: [
    CommonModule
  ]
})
export class VulModule { }
